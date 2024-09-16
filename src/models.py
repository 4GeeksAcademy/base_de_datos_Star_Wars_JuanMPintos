import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False, unique= True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(31), nullable=False, unique= True)
    password = Column(String(30), nullable=False)
    suscription_date = Column(Integer)

    relation_favorites = relationship('Favorites', backref=('user'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(30))

    relation_favorites= relationship('Favorites', backref=('character'))

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(30))

    relation_favorites = relationship('Favorites', backref=('planets'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    characterid = Column(Integer, ForeignKey('character.id'))
    planetsid = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
