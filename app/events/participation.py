from flask import session, request
from flask_socketio import join_room, leave_room
from app.services import room
from . import socketio


@socketio.on("join")
def on_join_game(data):
    game_id = data["game_id"]
    session["game_id"] = game_id

    # if not room.is_room_available(game_id):
    #     socketio.emit("participation", {"success": False, "message": "Room not available."}, to=request.sid)
    # else:

    join_room(game_id)
    socketio.emit("participation", {"success": True, "message": "A player has joined."}, to=game_id)


@socketio.on("disconnect")
def on_leave_game():
    print("Left")


@socketio.on("player_disconnect")
def on_leave_game():
    print("A player disconnected.")
    game_id = session["game_id"]

    leave_room(game_id)
    socketio.emit("participation", "A player has left.", to=game_id)


@socketio.on("cancel_join")
def on_cancel_join(game_id):
    print("Cancelling:", game_id)
    if room.number_of_participant(game_id) == 0:
        print("A room deleted.")
        room.remove_room(game_id)