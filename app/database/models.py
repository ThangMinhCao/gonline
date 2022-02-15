from . import db
from shortuuid import uuid

DEFAULT_PIECE_COLOR = "#F8BB84"


class Room(db.Model):
    __tablename__ = "room"

    id = db.Column(db.String, primary_key=True)
    participants = db.relationship(
        "Participant", backref="room", cascade="all, delete-orphan")
    current_player = db.Column(db.String)
    moves = db.relationship("Move", back_populates="room")
    started = db.Column(db.Boolean, nullable=False)
    ended = db.Column(db.Boolean, nullable=False)

    def __init__(self):
        self.id = uuid()
        self.started = False
        self.ended = False


class Participant(db.Model):
    __tablename__ = "participant"

    id = db.Column(db.String, primary_key=True)
    room_id = db.Column(db.String, db.ForeignKey("room.id"), nullable=False)
    moves = db.relationship(
        "Move", back_populates="player", cascade="all, delete-orphan")
    is_host = db.Column(db.Boolean, default=False)
    color = db.Column(db.String, default=DEFAULT_PIECE_COLOR)

    def __init__(self, room_id):
        self.id = uuid()
        self.room_id = room_id
        if not Room.query.filter_by(id=room_id).first().participants:
            self.is_host = True
            self.color = "#000000"


class Move(db.Model):
    __tablename__ = "move"

    i = db.Column(db.Integer, primary_key=True)
    j = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.String, db.ForeignKey("room.id"), primary_key=True)
    room = db.relationship("Room", back_populates="moves")
    player_id = db.Column(db.ForeignKey("participant.id"), nullable=False)
    player = db.relationship(
        "Participant", back_populates="moves", lazy="subquery")

    def __init__(self, i, j, room_id, player_id):
        self.i = i
        self.j = j
        self.room_id = room_id
        self.player_id = player_id
