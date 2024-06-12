from flask import Blueprint, jsonify, request
from firebase_admin import db

from . import test_module

@test_module.route('/add/<collection_name>', methods=['POST'])
def add_data(collection_name):
    try:
        data = request.json
        ref = db.reference(f'/{collection_name}')
        ref.push(data)
        return jsonify({"success": True, "message": "Data added successfully."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@test_module.route('/get/<collection_name>', methods=['GET'])
def get_data(collection_name):
    try:
        ref = db.reference(f'/{collection_name}')
        data = ref.get()
        if data is None:
            return jsonify({"success": False, "message": "Collection not found."}), 404
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

@test_module.route('/update/<collection_name>', methods=['PUT'])
def update_data(collection_name):
    try:
        data = request.json
        ref = db.reference(f'/{collection_name}')
        data = ref.get()
        if data is None:
            return jsonify({"success": False, "message": "Collection not found."}), 404
        ref.update(data)
        return jsonify({"success": True, "message": "Data updated successfully."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500