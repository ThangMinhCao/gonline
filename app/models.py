from app.database.connector import db
import shortuuid


class Game(db.Model):
    __tablename__ = "game"

    id = db.Column(db.String, primary_key=True)
    participants = db.relationship("Participant", backref="game")
    moves = db.relationship("Move", backref="game")
    ended = db.Column(db.Boolean, nullable=False)

    def __init__(self):
        self.id = shortuuid.uuid()
        self.ended = False


class Participant(db.Model):
    __tablename__ = "participant"

    id = db.Column(db.String, primary_key=True)
    game_id = db.Column(db.String, db.ForeignKey("game.id"), nullable=False)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name="Unknown"):
        self.id = shortuuid.uuid()
        self.name = name


class Move(db.Model):
    __tablename__ = "move"

    x = db.Column(db.Integer, primary_key=True)
    y = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String, db.ForeignKey("game.id"), primary_key=True)

    def __init__(self, x, y):
        self.x = x
        self.y = y