from flask import Blueprint

key_module =  Blueprint('key_module', __name__)

from . import KeyController
