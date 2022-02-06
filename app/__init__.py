from flask import Flask
from flask_cors import CORS
from app.services import service_blueprint
from app.routes import route_blueprint
from app.events import event_blueprint
from app.events.events import socketio
from app.database.connector import init_database 

cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret!"
    app.register_blueprint(service_blueprint)
    app.register_blueprint(route_blueprint)
    app.register_blueprint(event_blueprint)
    # app = Flask(__name__, template_folder='./templates')

    init_database(app)
    socketio.init_app(app)
    cors.init_app(app)

    return app