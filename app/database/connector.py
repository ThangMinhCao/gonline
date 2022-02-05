from flask_sqlalchemy import SQLAlchemy
import os
from settings import DATABASE_URI

db = SQLAlchemy()


def init_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)