from flask import session
from app.database.controller import query_first_by_id
from app.database.models import Participant

from app.services.gameplay import move
from . import socketio


@socketio.on("move")
def on_move(data):
        game_id = session["game_id"]
        pos = (data["i"], data["j"])
        player_id = data["player_id"]
        new_move = move(game_id, player_id, pos)

        if new_move:
            socketio.emit("move",
                          { "position": pos,
                            "player_id": player_id,
                            "color": new_move.player.color },
                          to=game_id)