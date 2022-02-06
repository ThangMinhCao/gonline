from flask import Blueprint

event_blueprint = Blueprint("events", __name__)

from . import events
