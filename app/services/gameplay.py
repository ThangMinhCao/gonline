from app.models import Move
from app.database.connector import db


def move(game_id, player_id, pos):
    """
    Play a move
    :param game_id: string
    :param player_id: string
    :param pos: (x: int, y: int) 
    """
    x, y = pos
    new_move = Move(x, y, game_id, player_id)
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