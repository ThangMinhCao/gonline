from flask import render_template, jsonify
from app.services import room, auth
from app.database.models import Game, Participant
from app.database.controller import query_first_by_id
from settings import PUBLIC_URL
from . import route_blueprint


@route_blueprint.route("/game", methods=["POST"])
def on_create_room():
    try:
        game_id = room.add_room().id
        host_id = room.add_player(game_id)
        return jsonify(auth.encode_token(game_id, host_id))
    except Exception as err:
        return "Error", 300 


@route_blueprint.route("/game/<game_id>", methods=["POST"])
def on_join_room(game_id):
    if not room.is_room_available(game_id):
        return "This room is not available.", 400

    player_id = room.add_player(game_id)
    return jsonify(auth.encode_token(game_id, player_id))


@route_blueprint.route("/<token>", methods=["GET"])
def render_game_page(token):
    try:
        payload = auth.decode_token(token)
        game_id = payload["game_id"]
        player_id = payload["player_id"]
        queried_game = query_first_by_id(Game, game_id)
        queried_participant = query_first_by_id(Participant, player_id)
        played_moves = []

        if queried_game == None or queried_participant == None:
            raise ValueError("Invalid token.")

        if queried_game.started:
            played_moves = list(map(lambda move: (move.i, move.j, move.player.color), queried_game.moves))

        return render_template("game.html",
                               game_id=game_id,
                               player_id=player_id,
                               moves=played_moves,
                               is_host=queried_participant.is_host,
                               started=queried_game.started,
                               public_url=PUBLIC_URL)
    except ValueError as err:
        return str(err), 400


@route_blueprint.route("/")
@route_blueprint.route("/home")
def render_home():
    return render_template("index.html")
