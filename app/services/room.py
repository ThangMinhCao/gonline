from app.database.connector import db
from app.models import Game, Participant


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
    :return: Participant object created
    """
    new_player = Participant(game_id)
    db.session.add(new_player)
    db.session.commit()


def is_room_available(game_id):
    """
    Check if a game room is available
    :param game_id: string
    :return: boolean
    """
    return not (
        Game.query.filter_by(id=game_id).first() == None or
        len(Participant.query.all()) == 2
    )
