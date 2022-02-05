from flask import redirect, render_template, request, url_for
from . import route_blueprint
from app.models import Game
from app.database.connector import db

@route_blueprint.route("/game", methods=["GET", "POST"])
def game():
  if request.method == "GET":
    return render_template("game.html")

  # create a room game in DB
  new_game = Game()
  db.session.add(new_game)
  db.session.commit()
  print("New room created.")
  return {"room_id": 123456789}

@route_blueprint.route("/")
@route_blueprint.route("/home")
def home():
  return render_template("index.html")