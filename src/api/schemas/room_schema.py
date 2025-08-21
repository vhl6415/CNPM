from marshmallow import Schema, fields

class RoomSchema(Schema):
    id = fields.Int(dump_only=True)
    room_number = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str(required=True, description="Status: available, occupied, maintenance")