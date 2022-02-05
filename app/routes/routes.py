from . import route_blueprint

@route_blueprint.route('/game', methods=['POST'])
def create_game():
  # create a room game in DB
  print("New room created.")
  return
