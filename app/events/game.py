from flask import session

from app.services.gameplay import move
from . import socketio


@socketio.on("move")
def on_move(data):
    game_id = session["game_id"]
    pos = (data["i"], data["j"])
    player_id = data["player_id"]

    if move(game_id, player_id, pos):
        socketio.emit("move", { "position": pos, "player_id": player_id }, to=game_id)