from marshmallow import Schema, fields

class PetRequestSchema(Schema):
    name = fields.Str(required=True, description="Name")
    species = fields.Str(required=True, description="Species")
    age = fields.Int(required=True, description="Age")
    owner_id = fields.Int(required=True, description="ID of owner")


class PetResponseSchema(PetRequestSchema):
    id = fields.Int(dump_only=True, description="ID of pet")