from flask import current_app
import random

def generate_practice_exercises(user_id, topic, difficulty='medium'):
    """Generate personalized practice exercises based on user's level."""
    
    def get_user_level(user_id, topic):
        # Get user's proficiency level in the topic
        user_progress = current_app.db.user_progress.find_one(
            {'user_id': user_id, 'topic': topic}
        )
        return user_progress.get('level', 'beginner') if user_progress else 'beginner'
    
    def adjust_difficulty(base_difficulty, user_level):
        difficulty_levels = ['beginner', 'intermediate', 'advanced']
        current_level = difficulty_levels.index(user_level)
        
        if base_difficulty == 'easy':
            return max(0, current_level - 1)
        elif base_difficulty == 'hard':
            return min(2, current_level + 1)
        return current_level
    
    try:
        user_level = get_user_level(user_id, topic)
        adjusted_level = adjust_difficulty(difficulty, user_level)
        
        # Get exercises from database or generate them
        exercises = current_app.db.exercises.find({
            'topic': topic,
            'difficulty': adjusted_level
        }).limit(5)
        
        return [{
            'question': ex['question'],
            'options': ex.get('options', []),
            'type': ex.get('type', 'multiple_choice'),
            'hint': ex.get('hint')
        } for ex in exercises]
        
    except Exception as e:
        print(f"Error generating exercises: {str(e)}")
        return [] 