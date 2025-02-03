from flask import Blueprint, request, jsonify

bp = Blueprint('chat', __name__, url_prefix='/api/chat')

@bp.route('/', methods=['POST'])
def chat():
    return jsonify({"message": "Chat endpoint"}), 200 