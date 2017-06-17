"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from flask_server import session
from project import app
from project.database.make_database import Formula, User


@app.route('/user')
def printUsers():
    try:
        session.user
    except:
        return redirect(url_for('login'))

    formulas = session.query(User).all()
    return render_template('user_templates/creation_menu.html', formulas=formulas)


@app.route('/user/new', methods=['GET', 'POST'])
def newUser():
    try:
        session.user
    except:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new = Formula(name=request.form['name'])
        session.add(new)
        session.commit()
        flash(new.name + " was created")
        return redirect(url_for('printUsers'))
    else:
        return render_template('user_templates/new_user.html')

# Task 2: Create route for editMenuItem function here


@app.route('/user/<int:user_id>/edit/', methods=['GET', 'POST'])
def editUser(user_id):
    try:
        session.user
    except:
        return redirect(url_for('login'))

    editable = session.query(Formula).filter_by(id=user_id).one()
    if request.method == 'POST':
        editable.name = request.form['name']
        session.add(editable)
        session.commit()
        flash(editable.name + " was updated")
        return redirect(url_for('printUsers'))
    else:
        return render_template('user_templates/editUser.html', user_id=user_id, userName=editable.name, userTitle=editable.title)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/user/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteUser(user_id):
    try:
        session.user
    except:
        return redirect(url_for('login'))

    deletable = session.query(Formula).filter_by(id=user_id).one()
    if request.method == 'POST':
        session.delete(deletable)
        session.commit()
        flash(deletable.name + " was deleted")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('user_templates/deleteUser.html', formula_id=user_id, formulaName=deletable.name)