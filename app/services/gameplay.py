from app.database.models import Move
from app.database import db
from app.database.controller import query_move


def move(game_id, player_id, position):
    """
    Play a move
    :param game_id: string
    :param player_id: string
    :param position: (i: int, j: int) 
    """
    i, j = position

    if query_move(i, j, game_id):
        return False

    new_move = Move(i, j, game_id, player_id)
    db.session.add(new_move)
    db.session.commit()

    return True


def is_finished(game_id, pos):
    """
    Query moves and generate the current state of the board.
    Then check if game is finished after current move.
    :param game_id: string
    :param pos: (x: int, y: int) 
    :return: boolean
    """
    board = [[0]]
    return check_finished


def check_finished(board, pos):
    """
    Check if game is finished after current move.
    :param board: 2D 19 x 19 matrix of the game board
    :param pos: (x: int, y: int)
    """
    return False