from flask import Blueprint, request, jsonify

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Your route handlers here... 