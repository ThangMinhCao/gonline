from flask import Blueprint

service_blueprint = Blueprint("services", __name__)

from . import gameplay, room