from flask import Blueprint, jsonify, request, current_app
from app.services.recommendation_service import get_personalized_recommendations
from app.services.progress_service import get_learning_progress, get_skill_gaps
from app.utils.auth import require_auth
from datetime import datetime

bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')

@bp.route('/', methods=['GET'])
def get_dashboard():
    return jsonify({"message": "Dashboard endpoint"}), 200

@bp.route('/overview', methods=['GET'])
@require_auth
def get_dashboard_overview():
    user_id = request.user_id  # Set by auth middleware
    
    try:
        # Get all dashboard data
        progress = get_learning_progress(user_id)
        recommendations = get_personalized_recommendations(user_id)
        skill_gaps = get_skill_gaps(user_id)
        
        return jsonify({
            'progress': progress,
            'recommendations': recommendations,
            'skill_gaps': skill_gaps
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/goals', methods=['GET', 'POST'])
@require_auth
def handle_goals():
    user_id = request.user_id
    
    if request.method == 'GET':
        try:
            goals = current_app.db.goals.find({'user_id': user_id})
            return jsonify({'goals': list(goals)}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
            
    elif request.method == 'POST':
        try:
            new_goal = request.json
            new_goal['user_id'] = user_id
            result = current_app.db.goals.insert_one(new_goal)
            return jsonify({'message': 'Goal created', 'id': str(result.inserted_id)}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500 