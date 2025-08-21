from flask import Blueprint, request, jsonify
from api.schemas.pet_schema import PetRequestSchema, PetResponseSchema
from marshmallow import ValidationError

pet_bp = Blueprint('pet', __name__, url_prefix='/pets')

# Database tam thoi
pets = []
next_id = 1

@pet_bp.route('/', methods=['POST'])
def create_pet():
    global next_id
    try:
        data = PetRequestSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    data['id'] = next_id
    next_id += 1
    pets.append(data)
    return PetResponseSchema().dump(data), 201

@pet_bp.route('/', methods=['GET'])
def list_pets():
    return PetResponseSchema(many=True).dump(pets), 200

@pet_bp.route('/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if not pet:
        return jsonify({"message": "Pet not found"}), 404
    return PetResponseSchema().dump(pet), 200

@pet_bp.route('/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if not pet:
        return jsonify({"message": "Pet not found"}), 404
    try:
        data = PetRequestSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    pet.update(data)
    return PetResponseSchema().dump(pet), 200

@pet_bp.route('/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    global pets
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if not pet:
        return jsonify({"message": "Pet not found"}), 404
    pets = [p for p in pets if p['id'] != pet_id]
    return '', 204