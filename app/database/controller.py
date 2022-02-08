from app.database.models import Move


def query_first_by_id(table, id):
  return table.query.filter_by(id=id).first()


def query_move(i, j, game_id):
  return Move.query.filter_by(i=i, j=j, game_id=game_id).first()