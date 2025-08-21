from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from api.schemas.pet_schema import PetRequestSchema, PetResponseSchema
from api.schemas.booking_schema import BookingRequestSchema, BookingResponseSchema
from api.schemas.user_schema import UserSchema
from api.schemas.medical_schema import MedicalRecordSchema, AdmissionSchema
from api.schemas.room_schema import RoomSchema

spec = APISpec(
    title="Pet Health Care System",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Dang ki schema
spec.components.schema("PetRequest", schema=PetRequestSchema)
spec.components.schema("PetResponse", schema=PetResponseSchema)

spec.components.schema("BookingRequest", schema=BookingRequestSchema)
spec.components.schema("BookingResponse", schema=BookingResponseSchema)

spec.components.schema("User", schema=UserSchema)

spec.components.schema("MedicalRecord", schema=MedicalRecordSchema)
spec.components.schema("Admission", schema=AdmissionSchema)

spec.components.schema("Room", schema=RoomSchema)