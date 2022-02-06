from flask import Flask
from flask_cors import CORS
from app.routes import route_blueprint
from app.events.participation import socketio
from app.database.connector import init_database 

cors = CORS()


def create_app():
    app = Flask(__name__, template_folder="./templates")
    app.config["SECRET_KEY"] = "secret!"
    app.config["CORS_HEADERS"] = "Content-Type"
    app.register_blueprint(route_blueprint)

    init_database(app)
    socketio.init_app(app)
    cors.init_app(app)

    return app