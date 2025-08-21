from marshmallow import Schema, fields
from datetime import datetime

class BookingRequestSchema(Schema):
    pet_id = fields.Int(required=True, description="ID pet")
    customer_id = fields.Int(required=True, description="ID customer")
    veterinarian_id = fields.Int(required=False, allow_none=True, description="ID vet")
    booking_date = fields.DateTime(required=True, description="Date time")
    status = fields.Str(required=False, missing="pending", description="Status of booking (pending, confirmed, canceled)")

class BookingResponseSchema(BookingRequestSchema):
    id = fields.Int(dump_only=True, description="ID booking")
    created_at = fields.DateTime(dump_only=True, description="Created at booking")