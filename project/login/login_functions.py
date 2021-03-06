from manage import User
from flask import redirect, url_for, session
import logging
from flask_server import db


def is_valid(name, login):

    user = User.query.filter_by(name=name).one()

    if user:
        if user.id is int(login):
            logging.warn("login succussful")
            return True
        else:
            logging.warn("id does not equal code")
            return False
    else:
        logging.warn("user does not exsist")
        return False


def login_needed():
    try:
        if session.user:
            return
        else:
            return redirect(url_for('login'))
    except:
        return redirect(url_for('login'))