from datetime import datetime
from flask import jsonify, request
from firebase_admin import db
from .KeyModel import CreateActivationKeyDto,UpdateActivationKeyDto
from uuid import uuid4
from . import key_module


@key_module.route('/', methods=['POST'])
def post_key():
    try:
        data = request.json
        data = CreateActivationKeyDto(**data)
        ref = db.reference(f'/keys')
        payload = data.model_dump()
        payload['key'] = str(uuid4())
        payload['is_connected_once_desktop'] = False
        payload['is_connected_once_mobile'] = False
        payload['created_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        payload['updated_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        payload['expires_at'] = str(payload['expires_at']) 
        ref.push(payload)
        return jsonify({"success": True, "message": f"{payload['key']} Generated Successfully."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

@key_module.route('/<key_id>', methods=['PUT'])
def update_key(key_id):
    try:
        data = request.json
        data = UpdateActivationKeyDto(**data)
        ref = db.reference(f'/keys/{key_id}')
        current_data = ref.get()

        if not current_data:
            return jsonify({"success": False, "message": "Key not found"}), 404

        payload = data.model_dump()
        payload['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ref.update(payload)
        return jsonify({"success": True, "message": f"{payload['key']} Updated Successfully."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

@key_module.route('/<key_id>', methods=['DELETE'])
def delete_key(key_id):
    try:
        ref = db.reference(f'/keys/{key_id}')
        current_data = ref.get()
        if not current_data:
            return jsonify({"success": False, "message": "Key not found"}), 404
        ref.delete()
        return jsonify({"success": True, "message": f"{current_data['key']} Deleted Successfully."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500