from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_URI

db = SQLAlchemy()


def init_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)