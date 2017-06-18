"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for, session
from project import app
from manage import Formula, User
from project.login.login_functions import login_needed
import logging
from flask_server import db


@app.route('/formula')
def printFormulas():

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    formulas = Formula.query.all()
    return render_template('layout.html', formulas=formulas)


@app.route('/formula/new', methods=['GET', 'POST'])
def newFormula():

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    if request.method == 'POST':
        new = Formula(name=request.form['name'], description=request.form['description'])
        db.session.add(new)
        db.session.commit()
        flash(new.name + " was created")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('formula_templates/newFormula.html')

# Task 2: Create route for editMenuItem function here


@app.route('/formula/<int:formula_id>/edit/', methods=['GET', 'POST'])
def editFormula(formula_id):

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    editable = Formula.query.filter_by(id=formula_id).one()
    if request.method == 'POST':
        editable.description = request.form['description']
        db.session.add(editable)
        db.session.commit()
        flash(editable.name + " was updated")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('formula_templates/editFormula.html', formula_id=formula_id, formulaName=editable.name, formulaDescription=editable.description)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/formula/<int:formula_id>/delete/', methods=['GET', 'POST'])
def deleteFormula(formula_id):

    try:
        db.session.user
    except:
        return redirect(url_for('login'))


    deletable = Formula.query.filter_by(id=formula_id).one()
    if request.method == 'POST':
        db.session.delete(deletable)
        db.session.commit()
        flash(deletable.name + " was deleted")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('formula_templates/deleteFormula.html', formula_id=formula_id, formulaName=deletable.name)

