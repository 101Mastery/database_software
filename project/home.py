"""
Routes and views for the flask application.
"""

from project.database.users.models import User
from flask import render_template, redirect, url_for, request
from project import app


@app.route('/')
@app.route('/home')
def home():
    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    return render_template('home.html', user=user)