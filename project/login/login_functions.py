from functools import wraps
from flask import request, redirect, url_for
from project.database.users.models import User
import logging



def is_valid(name, login):
    user = User.query.filter_by(user_name=name).one()

    if user:
        if user.password == login:
            return True
        else:
            logging.warn("id does not equal code")
            return False
    else:
        logging.warn("user does not exsist")
        return False


def req_login():
    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
        return
    except:
        return redirect(url_for('login'))