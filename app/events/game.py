from flask import session
from . import socketio
from app.services.gameplay import move, start_game, valid_move


@socketio.on("move")
def on_move(data):
    game_id = session["game_id"]
    pos = (data["i"], data["j"])
    player_id = data["player_id"]

    if not valid_move(pos, game_id, player_id):
        return

    new_move, is_finished = move(game_id, player_id, pos)
    socketio.emit("move",
                  { "position": pos,
                    "player_id": player_id,
                    "color": new_move.player.color,
                    "next_player": new_move.game.current_player,
                    "is_finished": is_finished },
                  to=game_id)


@socketio.on("start_game")
def on_start_game(game_id):
    current_player = start_game(game_id)
    socketio.emit("game_started", current_player, to=game_id)
