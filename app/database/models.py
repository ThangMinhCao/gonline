from . import db
from shortuuid import uuid


class Game(db.Model):
    __tablename__ = "game"

    id = db.Column(db.String, primary_key=True)
    participants = db.relationship("Participant", backref="game")
    moves = db.relationship("Move", backref="game")
    started = db.Column(db.Boolean, nullable=False)
    ended = db.Column(db.Boolean, nullable=False)

    def __init__(self):
        self.id = uuid()
        self.started = False
        self.ended = False


class Participant(db.Model):
    __tablename__ = "participant"

    id = db.Column(db.String, primary_key=True)
    game_id = db.Column(db.String, db.ForeignKey("game.id"), nullable=False)
    moves = db.relationship("Move", backref="participant")
    is_host = db.Column(db.Boolean, default=False)

    def __init__(self, game_id):
        self.id = uuid()
        self.game_id = game_id
        if not Game.query.filter_by(id=game_id).first().participants:
            self.is_host = True


class Move(db.Model):
    __tablename__ = "move"

    i = db.Column(db.Integer, primary_key=True)
    j = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String, db.ForeignKey("game.id"), primary_key=True)
    player_id = db.Column(db.ForeignKey("participant.id"), nullable=False)

    def __init__(self, i, j, game_id, player_id):
        self.i = i
        self.j = j
        self.game_id = game_id
        self.player_id = player_id