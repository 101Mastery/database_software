from os import environ
from project import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kmbarubaepxomi:af79f014f68830f6cb2d50141eedb08cef174f75f08908df61949eae84c2da9b@ec2-54-225-182-108.compute-1.amazonaws.com:5432/d37ahe0r1okrdd'
db = SQLAlchemy(app)
app.secret_key = 'super_secret'
db.session.login = True
db.session.user = None

if __name__=='__main__':
    app.secret_key = 'super_secret'
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)




