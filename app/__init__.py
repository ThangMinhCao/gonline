from flask import Flask
from flask_socketio import SocketIO, emit
from .services import service_blueprint
from .events import database_blueprint

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    app.register_blueprint(service_blueprint)
    app.register_blueprint(database_blueprint)

    socketio.init_app(app)

    return app

# @socketio.on('join')
# def on_join_room(json, methods=['GET', 'POST']):
#     print('received event: ' + str(json))
#     socketio.emit('A new user joined')