from .connector import db
from sqlalchemy import Boolean, Column, String, Integer, ARRAY
from sqlalchemy.dialects import postgresql


class Game(db):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)


class Player(db):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
