from flask import Blueprint

socket_event_blueprint = Blueprint('database', __name__)

from . import events