from os import environ
from project import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_server import db


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Formula(db.Model):
    __tablename__ = 'formula'

    name = db.Column(db.String(80), nullable = False)

    id = db.Column(db.Integer, primary_key = True)

    description = db.Column(db.String(250))


class User(db.Model):
    __tablename__ = 'user'

    name = db.Column(db.String(80), nullable = False)

    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String(80))

    user_creator = db.Column(db.Boolean, default = True)

    def get_id(self):
        return self.id


if __name__=='__main__':
    manager.run()
