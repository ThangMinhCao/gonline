from flask import redirect, url_for
from . import route_blueprint
from ..models import Game
from ..database import db

@route_blueprint.route('/game', methods=['POST', 'GET'])
def create_game():
  # create a room game in DB
  new_game = Game()
  db.session.add(new_game)
  db.session.commit()
  print("New room created.")
  return {'room_id': 123456789}