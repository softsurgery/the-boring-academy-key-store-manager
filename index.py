from flask import Flask, jsonify, redirect, render_template, request, url_for
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, db
from modules.TestModule import test_module

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

cred = credentials.Certificate(os.getenv('FIREBASE_ADMIN_SDK'))
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL')
})

app.register_blueprint(test_module, url_prefix='/test')

@app.route('/')
def index():
    return 'Hello, Flask with Firebase!'



@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({"success": False, "message": "Name and Email are required."}), 400

    # Push data to Firebase Realtime Database
    ref = db.reference('/access-key')
    new_data = ref.push({
        'name': name,
        'email': email
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.getenv('FLASK_RUN_PORT', 5001))  # Default to 5000 if not set
    app.run(debug=True, port=port)
