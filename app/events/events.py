from flask_socketio import join_room, leave_room
from .. import socketio


@socketio.on('join')
def on_join(game_id, player_id):
    print(f'Player {player_id} just joined {game_id}')
    join_room(game_id)