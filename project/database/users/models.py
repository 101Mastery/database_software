from flask_server import db
from uuid import uuid4


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80), nullable = False)

    id = db.Column(db.Integer, primary_key = True)

    password = db.Column(db.String(80), nullable=True, default=id)

    user_name = db.Column(db.String(80), nullable=True, default=name)

    title = db.Column(db.String(80))

    key = db.Column(db.String(80), default=uuid4())