from flask import render_template, make_response, request, redirect, url_for, flash
from project import app
from project.login.login_functions import is_valid
from project.database.users.models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        name = request.form['name']

        password = request.form['password']

        try:
            res = is_valid(name, password)
        except:
            res = False

        if res:
            user = User.query.filter_by(user_name=request.form['name']).one()

            response = make_response(redirect(url_for('home')))
            response.set_cookie('UserCookie', request.form['name'])

            return response

        else:
            flash("invalid username or password")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('UserCookie')

    return response


