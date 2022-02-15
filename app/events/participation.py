from flask import session, request
from flask_socketio import join_room, leave_room
from app.database.controller import query_first_by_id
from app.database.models import Room
from app.services.gameplay import is_game_started
from . import socketio


@socketio.on("connect")
def on_connect():
    """
    Handle Socket.IO connection of a client
    """
    room_id = request.args.get("room_id")
    game = query_first_by_id(Room, room_id)

    if not game:
        return False

    session["room_id"] = room_id
    join_room(room_id)
    socketio.emit("player_joined", len(game.participants) == 2, to=room_id)

    if is_game_started(room_id):
        socketio.emit("game_started", game.current_player, to=room_id)


@socketio.on("player_disconnect")
def on_leave_game():
    """
    Handle leave game event of a client
    """
    room_id = session["room_id"]

    leave_room(room_id)
    socketio.emit("participation", "A player has left.", to=room_id)
