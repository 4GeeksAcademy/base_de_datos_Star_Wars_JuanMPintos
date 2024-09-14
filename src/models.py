import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    user_name = Column(String(20), nulleable= False, unique= True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nulleable=False)
    email = Column(String(30), nulleable=False, unique= True)
    password = Column(String(30), nulleable=False)
    suscription_date = Column(Datename)

class Character(Base):
    __tablename__ = 'character'
    characterid = Column(Integer, primary_key=True)
    character_name = Column(String(30))

class Planets(Base):
    __tablename__= 'planets'
    planetsid = Column(Integer, primary_key=True)
    planet_name = Column(String(30))

class Favorites(Base):
    __tablename__ = ' favorites'
    favoritesid = Column(Integer, primary_key=True)
    characterid = Column(Integer)
    planetsid = Column(Integer)


 def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
