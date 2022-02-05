from database.connector import db
# from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, ARRAY


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True, index=True)
    # participants = db.Column(db.Integer, db.ForeignKey('.id'))
    participants = db.relationship('Participant', backref='game', lazy=True)

class Participant(db.Model):
    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True, index=True)

class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
