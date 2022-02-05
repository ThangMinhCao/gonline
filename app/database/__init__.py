from flask import Blueprint

database_blueprint = Blueprint("database", __name__)

from . import connector, controller
# from .connector import db, init_database