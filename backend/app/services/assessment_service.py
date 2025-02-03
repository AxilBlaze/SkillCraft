from flask import current_app
import random
from datetime import datetime

def get_adaptive_assessment(user_id, topic):
    """Generate an adaptive assessment based on user's current level."""
    
    def get_user_level(user_id, topic):
        user_progress = current_app.db.user_progress.find_one(
            {'user_id': user_id, 'topic': topic}
        )
        return user_progress.get('level', 'beginner') if user_progress else 'beginner'
    
    def select_questions(topic, level, count=5):
        # Get questions from database based on topic and difficulty
        questions = list(current_app.db.questions.find({
            'topic': topic,
            'difficulty': level
        }).limit(count))
        
        return questions
    
    try:
        user_level = get_user_level(user_id, topic)
        questions = select_questions(topic, user_level)
        
        # Create assessment
        assessment = {
            'user_id': user_id,
            'topic': topic,
            'level': user_level,
            'questions': [{
                'id': str(q['_id']),
                'question': q['question'],
                'options': q.get('options', []),
                'type': q.get('type', 'multiple_choice')
            } for q in questions]
        }
        
        return assessment
    except Exception as e:
        print(f"Error generating assessment: {str(e)}")
        return None 

def save_assessment_result(data):
    """Save assessment results to database."""
    try:
        # Create assessment result document
        assessment_result = {
            'user_id': data.get('user_id'),
            'answers': data.get('answers'),
            'score': data.get('score'),
            'topic': data.get('topic'),
            'timestamp': datetime.utcnow()
        }
        
        # Insert into database
        result = current_app.db.assessment_results.insert_one(assessment_result)
        
        return result
        
    except Exception as e:
        print(f"Error saving assessment result: {str(e)}")
        raise

def get_user_level(user_id, topic):
    """Get user's current level for a topic."""
    # Implement level determination logic
    return "beginner"  # Default level

def get_questions_for_level(topic, level):
    """Get assessment questions appropriate for the user's level."""
    # Implement question selection logic
    return [
        {
            "id": "q1",
            "question": "Sample question 1",
            "options": ["A", "B", "C", "D"],
            "difficulty": level
        }
    ] 