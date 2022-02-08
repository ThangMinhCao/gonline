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

    return (new_move, is_finished(new_move.game, (i, j)))


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


def is_finished(game, pos):
    """
    Query moves and generate the current state of the board.
    Then check if game is finished after current move.
    :param game_id: string
    :param pos: (x: int, y: int) 
    :return: boolean
    """
    move_set = set(map(lambda move: (move.i, move.j, move.player_id), game.moves))
    print(move_set)
    # return check_finished
    return False