from flask import session
from . import socketio


@socketio.on("move")
def on_move(data):
    player = session["player_name"]
    game_id = session["game_id"]
    pos = (data["x"], data["y"])

    # socketio.emit("participation", f"{player} has left.", to=game_id)
