from flask import Blueprint, request, jsonify
from api.schemas.room_schema import RoomSchema
from marshmallow import ValidationError

room_bp = Blueprint('room', __name__, url_prefix='/rooms')

rooms = []
next_id = 1

@room_bp.route('/', methods=['POST'])
def create_room():
    global next_id
    try:
        data = RoomSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    data['id'] = next_id
    next_id += 1
    rooms.append(data)
    return RoomSchema().dump(data), 201

@room_bp.route('/', methods=['GET'])
def list_rooms():
    return RoomSchema(many=True).dump(rooms), 200

@room_bp.route('/<int:room_id>', methods=['GET'])
def get_room(room_id):
    room = next((r for r in rooms if r['id'] == room_id), None)
    if not room:
        return jsonify({"message": "Room not found"}), 404
    return RoomSchema().dump(room), 200

@room_bp.route('/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    room = next((r for r in rooms if r['id'] == room_id), None)
    if not room:
        return jsonify({"message": "Room not found"}), 404
    try:
        data = RoomSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    room.update(data)
    return RoomSchema().dump(room), 200

@room_bp.route('/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    global rooms
    room = next((r for r in rooms if r['id'] == room_id), None)
    if not room:
        return jsonify({"message": "Room not found"}), 404
    rooms = [r for r in rooms if r['id'] != room_id]
    return '', 204