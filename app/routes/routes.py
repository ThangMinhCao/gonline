from flask import render_template, jsonify
from app.services import room, auth
from app.database.models import Room, Participant
from app.database.controller import query_first_by_id
from settings import PUBLIC_URL
from . import route_blueprint


@route_blueprint.route("/game", methods=["POST"])
def on_create_room():
    """
    Handle create room request.
    A new room is created along with the host player.
    :return: The token to join the room
    """
    room_id = room.add_room().id
    host_id = room.add_player(room_id)
    return jsonify(auth.encode_token(room_id, host_id))


@route_blueprint.route("/game/<room_id>", methods=["POST"])
def on_join_room(room_id):
    """
    Handle the join room request. 
    :return: The token to join the room
    """
    if not room.is_room_available(room_id):
        return "This room is not available.", 400

    player_id = room.add_player(room_id)
    return jsonify(auth.encode_token(room_id, player_id))


@route_blueprint.route("/<token>", methods=["GET"])
def render_game_page(token):
    """
    Handle the game page rendering using template.
    It query data to render the game's current state if it's already started.
    """
    try:
        payload = auth.decode_token(token)
        room_id = payload["room_id"]
        player_id = payload["player_id"]
        queried_game = query_first_by_id(Room, room_id)
        queried_participant = query_first_by_id(Participant, player_id)
        played_moves = []

        if queried_game == None or queried_participant == None:
            raise ValueError("Invalid token.")

        if queried_game.started:
            played_moves = list(
                map(lambda move: (move.i, move.j, move.player.color), queried_game.moves))

        return render_template("game.html",
                               room_id=room_id,
                               player_id=player_id,
                               moves=played_moves,
                               is_host=queried_participant.is_host,
                               public_url=PUBLIC_URL)
    except ValueError as err:
        return str(err), 400


@route_blueprint.route("/")
@route_blueprint.route("/home")
def render_home():
    return render_template("index.html")
