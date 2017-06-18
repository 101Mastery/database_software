"""
Routes and views for the flask application.
"""

from flask import render_template, redirect, url_for
from project import app
from flask_server import db


@app.route('/')
@app.route('/home')
def home():

    try:
        db.session.user
    except:
        return redirect(url_for('login'))

    return render_template('home.html')