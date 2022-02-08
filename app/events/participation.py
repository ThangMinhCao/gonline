from flask import session, request
from flask_socketio import join_room, leave_room
from app.database.controller import query_first_by_id
from app.database.models import Game
from app.services.gameplay import is_game_started
from . import socketio


@socketio.on("connect")
def on_connect():
    game_id = request.args.get("game_id")
    game = query_first_by_id(Game, game_id)

    if not game:
        return False  

    session["game_id"] = game_id
    join_room(game_id)
    socketio.emit("player_joined", len(game.participants) == 2, to=game_id)
    
    if is_game_started(game_id):
        socketio.emit("game_started", game.current_player, to=game_id)


@socketio.on("player_disconnect")
def on_leave_game():
    game_id = session["game_id"]

    leave_room(game_id)
    socketio.emit("participation", "A player has left.", to=game_id)