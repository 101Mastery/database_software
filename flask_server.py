from os import environ
from project import app
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from project.database.make_database import Base

engine = create_engine('sqlite:///project/database/formula.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__=='__main__':
    app.secret_key = 'super_secret'
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)