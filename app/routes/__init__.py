from flask import Blueprint

route_blueprint = Blueprint('routes', __name__)

from . import routes
