from flask import render_template, request, redirect, url_for,flash
from project import app
from project.login.login_functions import is_valid
from project.database.make_database import User
from flask_server import session
import logging


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        name = request.form['name']

        userid = request.form['code']

        try:
            res = is_valid(name, userid)
        except:
            res = False

        if res:
            logging.warn(name)
            user = session.query(User).filter_by(id=request.form['code']).one()
            session.user = user

            return redirect(url_for('home'))

        else:
            flash("invalid username or password")
            return render_template('login.html')
    else:
        return render_template('login.html')