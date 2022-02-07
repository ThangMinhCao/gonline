from flask import render_template, jsonify
from app.services import room
from . import route_blueprint


@route_blueprint.route("/game", methods=["POST"])
def on_create_room():
    return jsonify(room.add_room().id)


@route_blueprint.route("/game/<game_id>")
def render_game(game_id):
    return render_template("game.html", game_id=game_id)


@route_blueprint.route("/")
@route_blueprint.route("/home")
def render_home():
    return render_template("index.html")