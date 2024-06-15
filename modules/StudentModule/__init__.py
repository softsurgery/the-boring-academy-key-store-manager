from flask import Blueprint

student_module =  Blueprint('student_module', __name__)

from . import StudentController
