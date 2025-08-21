from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    role = fields.Str(required=True, description="Role: customer, staff, veterinarian, admin")
    password = fields.Str(load_only=True, required=True)
    created_at = fields.DateTime(dump_only=True)

class CustomerSchema(UserSchema):
    full_name = fields.Str(required=True)
    phone = fields.Str(required=True)
    address = fields.Str(required=True)

class StaffSchema(UserSchema):
    full_name = fields.Str(required=True)
    position = fields.Str(required=True)

class VeterinarianSchema(UserSchema):
    full_name = fields.Str(required=True)
    specialization = fields.Str(required=True)
