from flask import Blueprint, jsonify, request, current_app
from app.services.analytics_service import (
    get_performance_metrics,
    get_skills_progress,
    get_learning_patterns,
    get_improvement_suggestions
)
from app.utils.auth import require_auth
from datetime import datetime, timedelta

bp = Blueprint('analytics', __name__, url_prefix='/api/analytics')

@bp.route('/', methods=['GET'])
def get_analytics():
    return jsonify({"message": "Analytics endpoint"}), 200

@bp.route('/performance', methods=['GET'])
@require_auth
def get_performance():
    user_id = request.user_id
    time_range = request.args.get('range', 'month')  # week, month, year
    
    try:
        metrics = get_performance_metrics(user_id, time_range)
        return jsonify({
            'metrics': metrics,
            'time_range': time_range
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/skills-progress', methods=['GET'])
@require_auth
def get_progress():
    user_id = request.user_id
    
    try:
        progress = get_skills_progress(user_id)
        return jsonify({
            'overall_progress': progress.get('overall'),
            'by_category': progress.get('categories'),
            'recent_achievements': progress.get('recent_achievements')
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/learning-patterns', methods=['GET'])
@require_auth
def get_patterns():
    user_id = request.user_id
    
    try:
        patterns = get_learning_patterns(user_id)
        return jsonify({
            'study_patterns': patterns.get('study_patterns'),
            'engagement_metrics': patterns.get('engagement'),
            'preferred_times': patterns.get('preferred_times')
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/suggestions', methods=['GET'])
@require_auth
def get_suggestions():
    user_id = request.user_id
    
    try:
        suggestions = get_improvement_suggestions(user_id)
        return jsonify({
            'suggestions': suggestions.get('recommendations'),
            'focus_areas': suggestions.get('focus_areas'),
            'resource_recommendations': suggestions.get('resources')
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 