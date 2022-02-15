from app.database import db
from app.database.controller import query_first_by_id
from app.database.models import Room, Participant


def add_room():
    """
    Add a new room to DB 

    :return -> Room: The new Room object created
    """
    new_room = Room()
    db.session.add(new_room)
    db.session.commit()
    return new_room


def add_player(room_id):
    """
    Add a new player to DB 

    :param session_id -> str: request sid of the client
    :param room_id -> str: string
    :return -> str: Participant id
    """
    new_player = Participant(room_id)
    db.session.add(new_player)
    db.session.commit()
    return new_player.id


def remove_room(room_id):
    """
    Remove a game room

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    query_first_by_id(Room, room_id).delete()
    db.session.commit()


def is_room_available(room_id):
    """
    Check if a game room is available
    :param room_id: string
    :return: boolean
    """
    game_room = query_first_by_id(Room, room_id)
    return game_room and len(game_room.participants) < 2


def toggle_game_state(room_id, start=True):
    query_first_by_id(Room, room_id).started = start
