from functools import wraps
from flask import request, jsonify, current_app
from jose import jwt, JWTError

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'No authorization header'}), 401
        
        try:
            # Remove 'Bearer ' from token
            token = auth_header.split(' ')[1]
            # Verify token
            payload = jwt.decode(
                token,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            request.user_id = payload['sub']
            return f(*args, **kwargs)
        except JWTError:
            return jsonify({'error': 'Invalid token'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 500
            
    return decorated 