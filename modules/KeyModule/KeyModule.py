from datetime import datetime
from flask import Blueprint, jsonify, request
from firebase_admin import db
from .Models import ActivationKeyDto
from uuid import uuid4
from . import key_module


@key_module.route('/new', methods=['POST'])
def post_key():
    try:
        data = request.json
        data = ActivationKeyDto(**data)
        ref = db.reference(f'/keys')
        payload = data.model_dump()
        payload['key'] = str(uuid4())
        payload['is_connected_once_desktop'] = False
        payload['is_connected_once_mobile'] = False
        payload['created_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        payload['expires_at'] = str(payload['expires_at']) 
        ref.push(payload)
        return jsonify({"success": True, "message": f"{payload['key']} Generated Successfully."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500