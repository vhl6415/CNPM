from marshmallow import Schema, fields
from datetime import datetime

class MedicalRecordSchema(Schema):
    id = fields.Int(dump_only=True)
    pet_id = fields.Int(required=True)
    veterinarian_id = fields.Int(required=True)
    visit_date = fields.DateTime(required=True)
    diagnosis = fields.Str(required=True)
    treatment = fields.Str(required=True)
    notes = fields.Str()
    created_at = fields.DateTime(dump_only=True)

class AdmissionSchema(Schema):
    id = fields.Int(dump_only=True)
    pet_id = fields.Int(required=True)
    room_id = fields.Int(required=True)
    admission_date = fields.DateTime(required=True)
    discharge_date = fields.DateTime(allow_none=True)
    status = fields.Str(required=True, description="Status: admitted, discharged")
    notes = fields.Str()