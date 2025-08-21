from flask import Blueprint, request, jsonify
from api.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from datetime import datetime

user_bp = Blueprint('user', __name__, url_prefix='/users')

users = []
next_id = 1

@user_bp.route('/', methods=['POST'])
def create_user():
    global next_id
    try:
        data = UserSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check for unique username or email
    if any(u['username'] == data['username'] for u in users):
        return jsonify({"message": "Username already exists"}), 400
    if any(u['email'] == data['email'] for u in users):
        return jsonify({"message": "Email already exists"}), 400

    data['id'] = next_id
    data['created_at'] = datetime.utcnow()
    next_id += 1
    users.append(data)
    return UserSchema().dump(data), 201

@user_bp.route('/', methods=['GET'])
def list_users():
    return UserSchema(many=True).dump(users), 200

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return UserSchema().dump(user), 200

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404
    try:
        data = UserSchema().load(request.json, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    user.update(data)
    return UserSchema().dump(user), 200

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404
    users = [u for u in users if u['id'] != user_id]
    return '', 204