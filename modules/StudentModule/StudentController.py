from datetime import datetime
from uuid import uuid4
from flask import jsonify, request
from pydantic import ValidationError
from .StudentModel import CreateStudentDto
from firebase_admin import db
from . import student_module

@student_module.route('/', methods=['POST'])
def create_student():
    try:
        data = request.json
        data = CreateStudentDto(**data)
        id = str(uuid4())
        ref = db.reference(f'/students/{id}')
        payload = data.model_dump()
        payload['created_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        payload['updated_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        ref.set(payload)
        return jsonify({"success": True, "message": f"Student Generated Successfully."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500