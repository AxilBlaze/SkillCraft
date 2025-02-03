from flask import current_app
from datetime import datetime

def get_user_path(user_id):
    """Get user's learning path with progress and recommendations."""
    
    def calculate_progress(milestones):
        completed = sum(1 for m in milestones if m.get('status') == 'completed')
        return (completed / len(milestones)) * 100 if milestones else 0
    
    try:
        # Get user's current path
        user_path = current_app.db.learning_paths.find_one({'user_id': user_id})
        if not user_path:
            # Create default path if none exists
            user_path = create_default_path(user_id)
            
        milestones = user_path.get('milestones', [])
        progress = calculate_progress(milestones)
        
        # Get current milestone
        current_milestone = next(
            (m for m in milestones if m.get('status') == 'in_progress'),
            milestones[0] if milestones else None
        )
        
        # Generate next steps
        next_steps = generate_next_steps(user_id, current_milestone)
        
        return {
            'milestones': milestones,
            'progress': progress,
            'current_milestone': current_milestone,
            'next_steps': next_steps
        }
    except Exception as e:
        print(f"Error getting user path: {str(e)}")
        return None

def update_milestone(user_id, milestone_id, status, completion_date=None):
    """Update milestone status and trigger path recalculation."""
    try:
        result = current_app.db.learning_paths.update_one(
            {
                'user_id': user_id,
                'milestones.id': milestone_id
            },
            {
                '$set': {
                    'milestones.$.status': status,
                    'milestones.$.completion_date': completion_date
                }
            }
        )
        
        if result.modified_count > 0:
            # Recalculate path if needed
            recalculate_path(user_id)
            
        return True
    except Exception as e:
        print(f"Error updating milestone: {str(e)}")
        return False

def generate_skill_tree(user_id):
    """Generate a visual skill tree based on user's progress."""
    try:
        # Get user's completed skills
        completed_skills = current_app.db.user_skills.find(
            {'user_id': user_id, 'status': 'completed'}
        )
        
        # Get skill dependencies
        skill_tree = current_app.db.skill_tree.find()
        
        # Mark completed skills in the tree
        marked_tree = mark_completed_skills(skill_tree, completed_skills)
        
        return marked_tree
    except Exception as e:
        print(f"Error generating skill tree: {str(e)}")
        return None

def get_course_sequence(user_id, current_topic):
    """Generate personalized course sequence."""
    try:
        # Get user's progress and preferences
        user_progress = current_app.db.user_progress.find_one({'user_id': user_id})
        
        # Get available courses
        courses = list(current_app.db.courses.find({'topic': current_topic}))
        
        # Sort and filter courses based on user's level
        sequence = sort_courses_by_difficulty(courses, user_progress.get('level', 'beginner'))
        
        return sequence
    except Exception as e:
        print(f"Error getting course sequence: {str(e)}")
        return [] 