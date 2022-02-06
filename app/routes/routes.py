from flask import jsonify, render_template, send_from_directory

from . import route_blueprint
from app.models import Game
from app.database.connector import db


@route_blueprint.route("/game", methods=["POST"])
def create_game():
    # create a room game in DB
    new_game = Game()
    db.session.add(new_game)
    db.session.commit()
    return jsonify({"room_id": new_game.id})


@route_blueprint.route("/game/<game_id>")
def render_game():
    return render_template("game.html")


@route_blueprint.route("/")
@route_blueprint.route("/home")
def home():
    return render_template("index.html")