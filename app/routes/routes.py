from flask import redirect, render_template, jsonify
from app.services import room, auth
from . import route_blueprint


@route_blueprint.route("/game", methods=["POST"])
def on_create_room():
    game_id = room.add_room().id
    host_id = room.add_player(game_id)
    return jsonify(auth.encode_token(game_id, host_id))
 
    
@route_blueprint.route("/game/<game_id>", methods=["POST"])
def on_join_room(game_id):
    if not room.is_room_available(game_id):
        return "This room is not available.", 400
    
    player_id = room.add_player(game_id)
    return jsonify(auth.encode_token(game_id, player_id))
    # return render_template("game.html", game_id=game_id)

    
@route_blueprint.route("/<token>", methods=["GET"])
def render_game_page(token):
    try:
        payload = auth.decode_token(token);
        return render_template("game.html", game_id=payload["game_id"], player_id=payload["player_id"])
    except ValueError as err:
        return str(err), 400


@route_blueprint.route("/")
@route_blueprint.route("/home")
def render_home():
    return render_template("index.html")