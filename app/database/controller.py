from app.database.models import Move


def query_first_by_id(table, id):
    """
    Query a row of a table given the id

    :param table: reference to the table (Room, Participant)
    :return -> Room or Participant: the queried object
    """
    return table.query.filter_by(id=id).first()


def query_move(i, j, room_id):
    """
    Query a move given the position and room id

    :param i -> int: coordinate repsects to vertical axis
    :param j -> int: coordinate repsects to horizontal axis
    :param room_id: str: the room Id
    :return -> Move: the queried Move object
    """
    return Move.query.filter_by(i=i, j=j, room_id=room_id).first()
