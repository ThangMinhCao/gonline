from flask import session
from . import socketio
from app.services.gameplay import move, start_game, valid_move


@socketio.on("move")
def on_move(data):
    """
    Handle move event emission from a client

    :param data: {
        "room_id" -> str: Id of the game room,
        "player_id" -> str: Id of the player,
        "i" -> int: Coordination respects to vertical axis,
        "j" -> int: Coordination respects to horizontal axis,
    }
    """
    room_id = session["room_id"]
    position = (data["i"], data["j"])
    player_id = data["player_id"]

    if not valid_move(room_id, player_id, position):
        return

    new_move, is_finished = move(room_id, player_id, position)
    socketio.emit("move",
                  {"position": position,
                   "player_id": player_id,
                   "color": new_move.player.color,
                   "next_player": new_move.room.current_player,
                   "is_finished": is_finished},
                  to=room_id)


@socketio.on("start_game")
def on_start_game(room_id):
    """
    Handle start game emission from a host client

    :param room_id -> str: Id of the game
    """
    current_player = start_game(room_id)
    socketio.emit("game_started", current_player, to=room_id)
