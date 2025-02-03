from flask import Blueprint, jsonify, current_app
from datetime import datetime
from app.services.llm_service import get_ai_response
from app.services.vector_store import get_vector_store
import numpy as np

bp = Blueprint('test', __name__, url_prefix='/api/test')

@bp.route('/all', methods=['GET'])
def test_all():
    results = {
        'mongodb': test_mongodb(),
        'huggingface': test_huggingface(),
        'vector_store': test_vector_store()
    }
    
    all_passed = all(result['status'] == 'success' for result in results.values())
    
    return jsonify({
        'overall_status': 'success' if all_passed else 'failed',
        'tests': results
    }), 200 if all_passed else 500

def test_mongodb():
    """Test MongoDB connection and basic operations."""
    try:
        # Test write operation
        test_doc = {
            'message': 'Test document',
            'timestamp': datetime.utcnow()
        }
        insert_result = current_app.db.test_collection.insert_one(test_doc)
        
        # Test read operation
        read_result = current_app.db.test_collection.find_one({
            '_id': insert_result.inserted_id
        })
        
        # Clean up
        current_app.db.test_collection.delete_one({
            '_id': insert_result.inserted_id
        })
        
        return {
            'status': 'success',
            'message': 'MongoDB connection test successful',
            'details': {
                'write_successful': bool(insert_result.inserted_id),
                'read_successful': bool(read_result),
                'database_name': current_app.db.name
            }
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': 'MongoDB connection test failed',
            'error': str(e)
        }

def test_huggingface():
    """Test Hugging Face API connection."""
    try:
        # Test simple completion
        test_prompt = "What is 2+2? Answer in one word."
        response = get_ai_response(test_prompt)
        
        return {
            'status': 'success',
            'message': 'Hugging Face API test successful',
            'details': {
                'test_prompt': test_prompt,
                'response': response['text'],
                'model_id': current_app.config['MODEL_ID']
            }
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': 'Hugging Face API test failed',
            'error': str(e)
        }

def test_vector_store():
    """Test vector store operations."""
    try:
        vector_store = get_vector_store()
        
        # Test vector addition
        test_vector = np.random.rand(768).astype('float32')  # Create random test vector
        vector_store.add_vectors([test_vector])
        
        # Test vector search
        distances, indices = vector_store.search(test_vector, k=1)
        
        return {
            'status': 'success',
            'message': 'Vector store test successful',
            'details': {
                'vector_dimension': len(test_vector),
                'search_results': {
                    'distances': distances.tolist(),
                    'indices': indices.tolist()
                },
                'store_path': current_app.config['VECTOR_STORE_PATH']
            }
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': 'Vector store test failed',
            'error': str(e)
        }

@bp.route('/mongodb', methods=['GET'])
def test_mongodb_route():
    """Test only MongoDB connection."""
    result = test_mongodb()
    return jsonify(result), 200 if result['status'] == 'success' else 500

@bp.route('/huggingface', methods=['GET'])
def test_huggingface_route():
    """Test only Hugging Face API."""
    result = test_huggingface()
    return jsonify(result), 200 if result['status'] == 'success' else 500

@bp.route('/vector-store', methods=['GET'])
def test_vector_store_route():
    """Test only vector store operations."""
    result = test_vector_store()
    return jsonify(result), 200 if result['status'] == 'success' else 500

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200 