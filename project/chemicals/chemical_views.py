"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from project import app
from project.database.formula_chemicals.models import Chemical
from project.database.users.models import User
from flask_server import db


@app.route('/chemical')
def printChemicals():

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    chemicals = Chemical.query.all()
    return render_template('chemical_templates/printChemicals.html', chemicals=chemicals, user=user)


@app.route('/chemical/new', methods=['GET', 'POST'])
def newChemical():

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new = Chemical(name=request.form['name'], user_key=user.key, cas=request.form['cas'], beyond_use=request.form['beyond_use'], storage=request.form['storage'])

        if str(request.form['explosive']) is 'true':
            new.explosive = True

        if str(request.form['flammable']) is 'true':
            new.flammable = True

        if str(request.form['oxidizer']) is 'true':
            new.oxidizer = True

        if str(request.form['corrosive']) is 'true':
            new.corrosive = True

        if str(request.form['toxic']) is 'true':
            new.toxic = True

        db.session.add(new)
        db.session.commit()
        flash(new.name + " was created ")
        return redirect(url_for('printChemicals', user=user))
    else:
        return render_template('chemical_templates/newChemical.html', user=user)

# Task 2: Create route for editMenuItem function here


@app.route('/chemical/<int:chemical_id>/edit/', methods=['GET', 'POST'])
def editChemical(chemical_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    editable = Chemical.query.filter_by(id=chemical_id).one()
    if request.method == 'POST':
        editable.description = request.form['description']
        db.session.add(editable)
        db.session.commit()
        flash(editable.name + " was updated")
        return redirect(url_for('printChemicals', user=user))
    else:
        return render_template('chemicals_templates/editChemical.html', user=user, chemical_id=chemical_id, chemicalName=editable.name, formulaDescription=editable.description)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/chemical/<int:chemical_id>/delete/', methods=['GET', 'POST'])
def deleteChemical(chemical_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    deletable = Chemical.query.filter_by(id=chemical_id).one()
    if request.method == 'POST':
        db.session.delete(deletable)
        db.session.commit()
        flash(deletable.name + " was deleted")
        return redirect(url_for('printChemicals', user=user))
    else:
        return render_template('chemical_templates/deleteChemical.html', chemical_id=chemical_id, chemicalName=deletable.name, user=user)


@app.route('/chemical/<int:chemical_id>/view/', methods=['GET'])
def viewChemical(chemical_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    chemical = Chemical.query.filter_by(id=chemical_id).one()

    return render_template('chemical_templates/view_chemical.html', chemical_id=chemical_id, chemical=chemical, user=user)
