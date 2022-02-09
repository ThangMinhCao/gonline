from app.database import db
from app.database.controller import query_first_by_id
from app.database.models import Game, Participant


def add_room():
    """
    Add a new room to DB 
    :return: Game object created
    """
    new_game = Game()
    db.session.add(new_game)
    db.session.commit()
    return new_game


def add_player(game_id):
    """
    Add a new player to DB 
    :param session_id: request sid of the client
    :param game_id: string
    :return: Participant id
    """
    new_player = Participant(game_id)
    db.session.add(new_player)
    db.session.commit()
    return new_player.id


def remove_room(game_id):
    query_first_by_id(Game, game_id).delete()
    db.session.commit()


def is_room_available(game_id):
    """
    Check if a game room is available
    :param game_id: string
    :return: boolean
    """
    game_room = query_first_by_id(Game, game_id)
    return game_room and len(game_room.participants) < 2


def toggle_game_state(game_id, start=True):
    query_first_by_id(Game, game_id).started = start
