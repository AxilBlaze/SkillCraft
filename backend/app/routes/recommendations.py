from flask import Blueprint, request, jsonify

bp = Blueprint('recommendations', __name__, url_prefix='/api/recommendations')

@bp.route('/', methods=['GET'])
def get_recommendations():
    return jsonify({"message": "Recommendations endpoint"}), 200 