from flask import Blueprint

test_module =  Blueprint('test_module', __name__)

from . import TestModule