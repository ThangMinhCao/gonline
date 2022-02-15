import random
from app.database.models import Room, Move
from app.database import db
from app.database.controller import query_first_by_id, query_move


def start_game(room_id):
    """
    Start a game that has the provided id

    :param game_id -> str: Id of the game
    :return -> str: Id of the current (first) player of the game
    """
    room = query_first_by_id(Room, room_id)

    if room.started or len(room.participants) < 2:
        return

    room.started = True
    room.current_player = random.choice(room.participants).id
    db.session.commit()

    return room.current_player


def is_game_started(room_id):
    room = query_first_by_id(Room, room_id)
    return room and room.started


def move(room_id, player_id, position):
    """
    Play a move

    :param room_id -> string: the room Id
    :param player_id -> string: Id of the player doing the move
    :param position -> (i: int, j: int): the 2D position of the move
    """
    i, j = position

    new_move = Move(i, j, room_id, player_id)
    db.session.add(new_move)
    db.session.commit()

    switch_turn(new_move.room)

    return (new_move, is_finished(new_move.room, (i, j, player_id)))


def valid_move(room_id, player_id, position):
    """
    Check if a move is valid

    :param room_id -> string: the room Id
    :param player_id -> string: Id of the player doing the move
    :param position -> (i: int, j: int): the 2D position of the move
    :return -> boolean: the indicator that shows if the move is valid
    """

    i, j = position

    if i < 0 or j < 0 or i > 18 or j > 18:
        return False

    room = query_first_by_id(Room, room_id)

    return room and \
        room.started and \
        room.current_player == player_id and \
        query_move(i, j, room_id) == None


def switch_turn(room):
    """
    Switch turn of a room

    :param room -> Room: the Room object queried from database
    """
    next_player = next(filter(lambda player: player.id !=
                       room.current_player, room.participants))
    room.current_player = next_player.id
    db.session.commit()


def is_finished(room, move_info):
    """
    Query moves and generate the current state of the board.
    Then check if game is finished after current move.

    :param room_id -> string: the room Id
    :param move_info -> (i: int, j: int, player_id: str): info of the last move
    :return -> boolean: indicator if the game is finished
    """
    move_set = set(
        map(lambda move: (move.i, move.j, move.player_id), room.moves))

    base_directions = [(-1, 0), (-1, -1), (0, -1), (1, -1)]
    for dir in base_directions:
        if search_line(move_info, dir, move_set):
            db.session.delete(room)
            db.session.commit()
            return True

    # return check_finishedmove


def search_line(move_info, base_dir, move_set):
    """
    Check if 5 or more pieces are connected on a line.
    The algorithm expand two sides from info of the given move.

    :param move_info -> (i: int, j: int, player_id: str): info of the last move
    :param base_dir -> (y: int, x: int): the base direction to search
    :param move_set -> {(i: int, j: int, player_id: str)}: set of move info
    :return -> boolean: indicator if the line has 5 or more continuous pieces
    """
    count = count_continuous_pieces(move_info, base_dir, move_set) \
        + count_continuous_pieces(move_info, (-base_dir[0], -base_dir[1]), move_set) \
        - 1

    if count >= 5:
        return True


def count_continuous_pieces(move_info, dir, move_set):
    """
    Recursively count the number of continuous same pieces given move info

    :param move_info -> (i: int, j: int, player_id: str): info of the last move
    :param dir -> (y: int, x: int): the direction to check
    :param move_set -> {(i: int, j: int, player_id: str)}: set of move info
    :return -> int: the number of continuous pieces
    """

    i, j, player_id = move_info

    if i < 0 or j < 0 or i > 18 or j > 18 or (i, j, player_id) not in move_set:
        return 0

    return 1 + count_continuous_pieces((i + dir[0], j + dir[1], player_id), dir, move_set)
