"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for, session
from project import app
from manage import Formula, User
from flask_server import db


@app.route('/user')
def printUsers():

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    users = User.query.all()
    return render_template('user_templates/creation_menu.html', users=users)


@app.route('/user/new', methods=['GET', 'POST'])
def newUser():

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    if request.method == 'POST':
        import logging
        logging.warn(request.form['creation_user'])
        if request.form['creation_user'] == 'True':
            new = User(name=request.form['name'], title=request.form['title'], user_creator=True)
        else:
            new = User(name=request.form['name'], title=request.form['title'])
        db.session.add(new)
        db.session.commit()
        flash("User was created")
        return redirect(url_for('printUsers'))
    else:
        return render_template('user_templates/new_user.html')

# Task 2: Create route for editMenuItem function here


@app.route('/user/<int:user_id>/edit/', methods=['GET', 'POST'])
def editUser(user_id):

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    editable = session.query(Formula).filter_by(id=user_id).one()
    if request.method == 'POST':
        editable.name = request.form['name']
        db.session.add(editable)
        db.session.commit()
        flash(editable.name + " was updated")
        return redirect(url_for('printUsers'))
    else:
        return render_template('user_templates/editUser.html', user_id=user_id, userName=editable.name, userTitle=editable.title)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/user/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteUser(user_id):

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    deletable = session.query(Formula).filter_by(id=user_id).one()
    if request.method == 'POST':
        db.session.delete(deletable)
        db.session.commit()
        flash(deletable.name + " was deleted")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('user_templates/deleteUser.html', formula_id=user_id, formulaName=deletable.name)