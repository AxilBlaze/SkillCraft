from app.services.vector_store import get_vector_store
from flask import current_app

def get_personalized_recommendations(user_id):
    """Generate personalized learning recommendations for the user."""
    try:
        # Get user's learning history
        user_history = list(current_app.db.learning_history.find({'user_id': user_id}))
        
        # If no history, return default recommendations
        if not user_history:
            return get_default_recommendations()
        
        # Get embeddings for user's history
        embeddings = get_user_embeddings(user_history)
        
        # Use vector store to find similar content
        vector_store = get_vector_store()
        similar_content = find_similar_content(vector_store, embeddings)
        
        return format_recommendations(similar_content)
        
    except Exception as e:
        print(f"Error generating recommendations: {str(e)}")
        return get_default_recommendations()

def get_user_embeddings(history):
    """Convert user's learning history to embeddings."""
    # This is a placeholder - implement actual embedding generation
    return [0] * 768  # Return zero vector of dimension 768

def find_similar_content(vector_store, embeddings):
    """Find similar content using vector store."""
    try:
        distances, indices = vector_store.search(embeddings)
        return get_content_by_indices(indices)
    except Exception as e:
        print(f"Error finding similar content: {str(e)}")
        return []

def get_content_by_indices(indices):
    """Get content details from database using indices."""
    # This is a placeholder - implement actual content retrieval
    return []

def get_default_recommendations():
    """Get default recommendations for new users."""
    try:
        # Get some default beginner-level content
        default_content = list(current_app.db.learning_content.find({
            'level': 'beginner'
        }).limit(5))
        
        return format_recommendations(default_content)
    except Exception as e:
        print(f"Error getting default recommendations: {str(e)}")
        return {
            'next_lessons': [],
            'practice_exercises': [],
            'additional_resources': []
        }

def format_recommendations(content):
    """Format the recommendations into categories."""
    return {
        'next_lessons': content[:2] if content else [],
        'practice_exercises': content[2:4] if len(content) > 2 else [],
        'additional_resources': content[4:] if len(content) > 4 else []
    } 