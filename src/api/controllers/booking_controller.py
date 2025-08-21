from flask import Blueprint, request, jsonify
from api.schemas.booking_schema import BookingRequestSchema, BookingResponseSchema
from marshmallow import ValidationError
from datetime import datetime

booking_bp = Blueprint('booking', __name__, url_prefix='/bookings')

bookings = []
next_id = 1

@booking_bp.route('/', methods=['POST'])
def create_booking():
    global next_id
    try:
        data = BookingRequestSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    data['id'] = next_id
    data['created_at'] = datetime.utcnow()
    next_id += 1
    bookings.append(data)
    return BookingResponseSchema().dump(data), 201

@booking_bp.route('/', methods=['GET'])
def list_bookings():
    return BookingResponseSchema(many=True).dump(bookings), 200

@booking_bp.route('/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({"message": "Booking not found"}), 404
    return BookingResponseSchema().dump(booking), 200

@booking_bp.route('/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({"message": "Booking not found"}), 404
    try:
        data = BookingRequestSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    booking.update(data)
    return BookingResponseSchema().dump(booking), 200

@booking_bp.route('/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    global bookings
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({"message": "Booking not found"}), 404
    bookings = [b for b in bookings if b['id'] != booking_id]
    return '', 204