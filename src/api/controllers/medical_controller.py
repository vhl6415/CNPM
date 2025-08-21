from flask import Blueprint, request, jsonify
from api.schemas.medical_schema import MedicalRecordSchema, AdmissionSchema
from marshmallow import ValidationError
from datetime import datetime

medical_bp = Blueprint('medical', __name__, url_prefix='/medical')

medical_records = []
admissions = []

medical_next_id = 1
admission_next_id = 1

# Quan li ho so kham benh
@medical_bp.route('/records', methods=['POST'])
def create_medical_record():
    global medical_next_id
    try:
        data = MedicalRecordSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    data['id'] = medical_next_id
    data['created_at'] = datetime.utcnow()
    medical_next_id += 1
    medical_records.append(data)
    return MedicalRecordSchema().dump(data), 201

@medical_bp.route('/records', methods=['GET'])
def list_medical_records():
    return MedicalRecordSchema(many=True).dump(medical_records), 200

@medical_bp.route('/records/<int:record_id>', methods=['GET'])
def get_medical_record(record_id):
    record = next((r for r in medical_records if r['id'] == record_id), None)
    if not record:
        return jsonify({"message": "Medical record not found"}), 404
    return MedicalRecordSchema().dump(record), 200

# Quan li nhap vien
@medical_bp.route('/admissions', methods=['POST'])
def create_admission():
    global admission_next_id
    try:
        data = AdmissionSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    data['id'] = admission_next_id
    admission_next_id += 1
    admissions.append(data)
    return AdmissionSchema().dump(data), 201

@medical_bp.route('/admissions', methods=['GET'])
def list_admissions():
    return AdmissionSchema(many=True).dump(admissions), 200

@medical_bp.route('/admissions/<int:admission_id>', methods=['GET'])
def get_admission(admission_id):
    admission = next((a for a in admissions if a['id'] == admission_id), None)
    if not admission:
        return jsonify({"message": "Admission not found"}), 404
    return AdmissionSchema().dump(admission), 200

@medical_bp.route('/admissions/<int:admission_id>', methods=['PUT'])
def update_admission(admission_id):
    admission = next((a for a in admissions if a['id'] == admission_id), None)
    if not admission:
        return jsonify({"message": "Admission not found"}), 404
    try:
        data = AdmissionSchema().load(request.json, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    admission.update(data)
    return AdmissionSchema().dump(admission), 200