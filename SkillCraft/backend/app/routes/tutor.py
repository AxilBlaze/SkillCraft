from flask import Blueprint, jsonify, request, current_app
from app.services.llm_service import get_ai_response
from app.services.exercise_service import generate_practice_exercises
from app.utils.auth import require_auth

bp = Blueprint('tutor', __name__, url_prefix='/api/tutor')

@bp.route('/', methods=['POST'])
def get_tutor_response():
    return jsonify({"message": "Tutor endpoint"}), 200

@bp.route('/chat', methods=['POST'])
@require_auth
def chat():
    user_id = request.user_id
    data = request.json
    
    try:
        message = data.get('message')
        context = data.get('context', {})
        
        # Store the message in chat history
        chat_message = {
            'user_id': user_id,
            'message': message,
            'timestamp': datetime.utcnow(),
            'type': 'user'
        }
        current_app.db.chat_history.insert_one(chat_message)
        
        # Get AI response
        response = get_ai_response(message, context)
        
        # Store AI response
        ai_message = {
            'user_id': user_id,
            'message': response['text'],
            'timestamp': datetime.utcnow(),
            'type': 'ai'
        }
        current_app.db.chat_history.insert_one(ai_message)
        
        return jsonify({
            'response': response['text'],
            'explanation': response.get('explanation'),
            'suggestions': response.get('suggestions')
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/history', methods=['GET'])
@require_auth
def get_chat_history():
    user_id = request.user_id
    limit = int(request.args.get('limit', 50))
    
    try:
        history = current_app.db.chat_history.find(
            {'user_id': user_id}
        ).sort('timestamp', -1).limit(limit)
        
        return jsonify({'history': list(history)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/exercises', methods=['GET'])
@require_auth
def get_exercises():
    user_id = request.user_id
    topic = request.args.get('topic')
    difficulty = request.args.get('difficulty', 'medium')
    
    try:
        exercises = generate_practice_exercises(user_id, topic, difficulty)
        return jsonify({'exercises': exercises}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 