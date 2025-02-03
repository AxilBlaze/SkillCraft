from flask import Blueprint, jsonify, request, current_app
from app.services.path_service import (
    get_user_path,
    update_milestone,
    generate_skill_tree,
    get_course_sequence
)
from app.services.assessment_service import get_adaptive_assessment, save_assessment_result
from app.utils.auth import require_auth
from datetime import datetime

bp = Blueprint('learning_path', __name__, url_prefix='/api/learning-path')

@bp.route('/path', methods=['GET'])
@require_auth
def get_path():
    user_id = request.user_id
    
    try:
        path = get_user_path(user_id)
        return jsonify({
            'path': path,
            'current_milestone': path.get('current_milestone'),
            'progress': path.get('progress'),
            'next_steps': path.get('next_steps')
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/milestone/<milestone_id>', methods=['PUT'])
@require_auth
def update_user_milestone(milestone_id):
    user_id = request.user_id
    data = request.json
    
    try:
        status = data.get('status')
        completion_date = datetime.utcnow() if status == 'completed' else None
        
        updated = update_milestone(user_id, milestone_id, status, completion_date)
        return jsonify({'success': True, 'milestone': updated}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/skill-tree', methods=['GET'])
@require_auth
def get_skill_tree():
    user_id = request.user_id
    
    try:
        skill_tree = generate_skill_tree(user_id)
        return jsonify({'skill_tree': skill_tree}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/course-sequence', methods=['GET'])
@require_auth
def get_sequence():
    user_id = request.user_id
    current_topic = request.args.get('topic')
    
    try:
        sequence = get_course_sequence(user_id, current_topic)
        return jsonify({'sequence': sequence}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/assessment', methods=['GET', 'POST'])
@require_auth
def handle_assessment():
    user_id = request.user_id
    
    if request.method == 'GET':
        topic = request.args.get('topic')
        try:
            assessment = get_adaptive_assessment(user_id, topic)
            return jsonify({'assessment': assessment}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
            
    elif request.method == 'POST':
        try:
            data = request.get_json()
            
            # Validate required fields
            if not data or 'answers' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            # Add user_id to the data
            data['user_id'] = user_id
            
            # Save assessment result
            result = save_assessment_result(data)
            
            return jsonify({
                'message': 'Assessment submitted', 
                'id': str(result.inserted_id)
            }), 201
        
        except Exception as e:
            print(f"Error submitting assessment: {str(e)}")
            return jsonify({'error': 'Failed to submit assessment'}), 500 