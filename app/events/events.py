from flask_socketio import join_room, leave_room
from .. import socketio

@socketio.event
def connect(sid):
    print(sid, "connected")

@socketio.on("join")
# def join_game(game_id, player_id):
def join_game():
    print("JOINEDDDDDDD-------------------")
    # print(f"Player {player_id} just joined {game_id}")
    # join_room(game_id)

@socketio.on("leave")
def leave_game(game_id, player_id):
    print(f"Player {player_id} just joined {game_id}")
    join_room(game_id)