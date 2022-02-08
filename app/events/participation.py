from flask import session, request
from flask_socketio import join_room, leave_room
from app.database.controller import query_first_by_id
from app.database.models import Game
from app.services import room
from . import socketio


@socketio.on("connect")
def on_connect():
    game_id = request.args.get("game_id")

    session["game_id"] = game_id
    join_room(game_id)
    print("Joined", game_id)


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