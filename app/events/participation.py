from flask import session
from flask_socketio import join_room, leave_room, SocketIO

socketio = SocketIO()


@socketio.on("join")
def join_game(data):
    player, game_id = data["player_name"], data["game_id"]
    session["game_id"] = game_id
    session["player_name"] = player

    join_room(game_id)
    socketio.emit("participation", f"{player} has joined.", to=game_id)


@socketio.on("disconnect")
def leave_game():
    player, game_id = session["player_name"], session["game_id"]

    leave_room(game_id)
    socketio.emit("participation", f"{player} has left.", to=game_id)