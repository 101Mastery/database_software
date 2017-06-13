import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Formula(Base):
    __tablename__ = 'formula'

    name = Column(String(80), nullable = False)

    id = Column(Integer, primary_key = True)

    description = Column(String(250))

class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable = False)

    id = Column(Integer, primary_key = True)

    title = Column(String(80))

###### insert at end of file ######

engine = create_engine('sqlite:///formula.db')

Base.metadata.create_all(engine)