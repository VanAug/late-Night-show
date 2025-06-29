from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.models.user import User
from server.models import db

auth_bp = Blueprint("auth", __name__)

# Register with auth required
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    user = User(username=username)
    user.set_password(password)  
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201

# Login with auth required
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):  
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200

    return jsonify({"error": "Invalid credentials"}), 401
