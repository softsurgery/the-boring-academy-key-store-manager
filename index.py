from flask import Flask
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials
from flask_cors import CORS, cross_origin
from modules.TestModule import test_module
from modules.KeyModule import key_module
from modules.StudentModule import student_module

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

cred = credentials.Certificate(os.getenv('FIREBASE_ADMIN_SDK'))
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL')
})

app.register_blueprint(test_module, url_prefix='/test')
app.register_blueprint(key_module, url_prefix='/keys')
app.register_blueprint(student_module, url_prefix='/students')


@app.route('/')
@cross_origin()
def index():
    return 'Hello, Flask with Firebase!'

if __name__ == '__main__':
    port = int(os.getenv('FLASK_RUN_PORT', 5001))
    app.run(debug=True, port=port)
