from flask import session, request
from flask_socketio import join_room, leave_room
from app.services import room
from . import socketio


@socketio.on("join")
def on_join_game(data):
    game_id = data["game_id"]
    session["game_id"] = game_id

    print("Join roommm------------------", request.sid)

    if not room.is_room_available(game_id):
        socketio.emit("participation", {"success": False, "message": "Room not available."}, to=request.sid)
    else:
        room.add_player(game_id)

        join_room(game_id)
        socketio.emit("participation", {"success": True, "message": "A player has joined."}, to=game_id)


@socketio.on("player_disconnecting")
def on_leave_game():
    game_id = session["game_id"]

    leave_room(game_id)
    socketio.emit("participation", "A player has left.", to=game_id)