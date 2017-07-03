
from project import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_server import db


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Formula(db.Model):
    __tablename__ = 'formula'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80), nullable = False)

    id = db.Column(db.Integer, primary_key = True)

    description = db.Column(db.String(250))

    instructions = db.Column(db.String(1000))


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80), nullable = False)

    id = db.Column(db.Integer, primary_key = True)

    password = db.Column(db.String(80), nullable=True, default=id)

    user_name = db.Column(db.String(80), nullable=True, default=name)

    title = db.Column(db.String(80))

    user_creator = db.Column(db.Boolean, default = True)

    def get_password(self):
        return self.password


if __name__=='__main__':
    manager.run()
