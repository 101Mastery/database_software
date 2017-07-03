"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from project import app
from project.database.users.models import User
from flask_server import db


@app.route('/user')
def printUsers():
    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    users = User.query.all()
    return render_template('user_templates/creation_menu.html', users=users, user=user)


@app.route('/user/new', methods=['GET', 'POST'])
def newUser():

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    if request.method == 'POST':

        new = User(name=request.form['name'], title=request.form['title'], user_name=request.form['user_name'], password=request.form['password'],)

        db.session.add(new)
        db.session.commit()
        flash("User was created")
        return redirect(url_for('printUsers', user=user))
    else:
        return render_template('user_templates/new_user.html', user=user)

# Task 2: Create route for editMenuItem function here


@app.route('/user/<int:user_id>/edit/', methods=['GET', 'POST'])
def editUser(user_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    editable = User.query.filter_by(id=user_id).one()
    if request.method == 'POST':

        editable.name = request.form['name']

        editable.title = request.form['title']

        editable.user_name = request.form['user_name']

        editable.password = request.form['password']

        db.session.add(editable)
        db.session.commit()

        flash(editable.name + " was updated")
        return redirect(url_for('printUsers', user=user))
    else:
        return render_template('user_templates/edit_user.html', user_id=user_id, editable=editable, user=user)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/user/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteUser(user_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    deletable = User.query.filter_by(id=user_id).one()
    if request.method == 'POST':
        db.session.delete(deletable)
        db.session.commit()
        flash(deletable.name + " was deleted")
        return redirect(url_for('printUsers', user=user))
    else:
        return render_template('user_templates/delete_user.html', user_id=user_id, userName=deletable.name, user=user)