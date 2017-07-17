"""
Routes and views for the flask application.
"""

from project.database.users.models import User
from flask import render_template, redirect, url_for, request
from project import app
from flask_server import db


@app.route('/')
@app.route('/home')
def home():
    if db.session.login:
        try:
            user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
        except:
            return redirect(url_for('login'))
    else:
        user = None
    return render_template('home.html', user=user)
