from flask import render_template, request, redirect, url_for, flash, session
from project import app
from project.login.login_functions import is_valid
from manage import User
import logging
from flask_server import db


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
            user = User.query.filter_by(id=request.form['code']).one()
            db.session.user = user

            return redirect(url_for('home'))

        else:
            flash("invalid username or password")
            return render_template('login.html')
    else:
        return render_template('login.html')