from flask import jsonify, redirect, render_template, request, url_for
from . import route_blueprint
from app.models import Game
from app.database.connector import db


@route_blueprint.route("/game", methods=["POST"])
def game():
    # create a room game in DB
    new_game = Game()
    db.session.add(new_game)
    db.session.commit()
    return jsonify({"room_id": new_game.id})


@route_blueprint.route("/game/<game_id>", methods=["GET"])
def get_game(game_id):
    return render_template("game.html")


@route_blueprint.route("/")
@route_blueprint.route("/home")
def home():
    return render_template("index.html")