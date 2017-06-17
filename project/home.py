"""
Routes and views for the flask application.
"""

from flask import render_template, redirect, url_for
from flask_server import session
from project import app


@app.route('/')
@app.route('/home')
def home():
    try:
        session.user
    except:
        return redirect(url_for('login'))

    return render_template('home.html')