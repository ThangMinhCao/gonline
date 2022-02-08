import random
from app.database.models import Game, Move
from app.database import db
from app.database.controller import query_first_by_id, query_move


def start_game(game_id):
    game = query_first_by_id(Game, game_id)

    if game.started or len(game.participants) < 2:
        return

    game.started = True
    game.current_player = random.choice(game.participants).id
    db.session.commit()

    return game.current_player

    
def is_game_started(game_id):
    game = query_first_by_id(Game, game_id)
    return game and game.started


def move(game_id, player_id, position):
    """
    Play a move
    :param game_id: string
    :param player_id: string
    :param position: (i: int, j: int) 
    """
    i, j = position

    new_move = Move(i, j, game_id, player_id)
    db.session.add(new_move)
    db.session.commit()

    switch_turn(new_move.game)

    return (new_move, is_finished(new_move.game, (i, j, player_id)))


def valid_move(pos, game_id, player_id):
    i, j = pos

    if i < 0 or j < 0 or i > 18 or j > 18:
        return False

    game = query_first_by_id(Game, game_id)
    return game and \
           game.started and \
           game.current_player == player_id and \
           query_move(i, j, game_id) == None


def switch_turn(game):
    next_player = next(filter(lambda player: player.id != game.current_player, game.participants))
    game.current_player = next_player.id
    db.session.commit()


def is_finished(game, move_info):
    """
    Query moves and generate the current state of the board.
    Then check if game is finished after current move.
    :param game_id: string
    :param pos: (x: int, y: int) 
    :return: boolean
    """
    move_set = set(map(lambda move: (move.i, move.j, move.player_id), game.moves))

    base_directions = [(-1, 0), (-1, -1), (0, -1), (1, -1)]
    for dir in base_directions:
        if search_one_axis(move_info, dir, move_set):
            db.session.delete(game)
            db.session.commit()
            return True

    # return check_finishedmove


def search_one_axis(move_info, base_dir, move_set):
    count = count_continuous_pieces(move_info, base_dir, move_set) \
            + count_continuous_pieces(move_info, (-base_dir[0], -base_dir[1]), move_set) \
            - 1
    
    if count >= 5:
        return True


def count_continuous_pieces(move_info, dir, move_set):
    i, j, player_id = move_info

    if i < 0 or j < 0 or i > 18 or j > 18 or (i, j, player_id) not in move_set:
        return 0

    return 1 + count_continuous_pieces((i + dir[0], j + dir[1], player_id), dir, move_set)
    
    