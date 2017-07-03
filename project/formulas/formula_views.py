"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from project import app
from project.database.formula_chemicals.models import Formula
from project.database.users.models import User
from flask_server import db


@app.route('/formula')
def printFormulas():

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    formulas = Formula.query.all()
    return render_template('layout.html', formulas=formulas, user=user)


@app.route('/formula/new', methods=['GET', 'POST'])
def newFormula():

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new = Formula(name=request.form['name'], description=request.form['description'], instructions=request.form['instructions'], user_key=user.key)
        db.session.add(new)
        db.session.commit()
        flash(new.name + " was created ")
        return redirect(url_for('printFormulas', user=user))
    else:
        return render_template('formula_templates/newFormula.html', user=user)

# Task 2: Create route for editMenuItem function here


@app.route('/formula/<int:formula_id>/edit/', methods=['GET', 'POST'])
def editFormula(formula_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    editable = Formula.query.filter_by(id=formula_id).one()
    if request.method == 'POST':
        editable.description = request.form['description']
        db.session.add(editable)
        db.session.commit()
        flash(editable.name + " was updated")
        return redirect(url_for('printFormulas', user=user))
    else:
        return render_template('formula_templates/editFormula.html', user=user, formula_id=formula_id, formulaName=editable.name, formulaDescription=editable.description)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/formula/<int:formula_id>/delete/', methods=['GET', 'POST'])
def deleteFormula(formula_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    deletable = Formula.query.filter_by(id=formula_id).one()
    if request.method == 'POST':
        db.session.delete(deletable)
        db.session.commit()
        flash(deletable.name + " was deleted")
        return redirect(url_for('printFormulas', user=user))
    else:
        return render_template('formula_templates/deleteFormula.html', formula_id=formula_id, formulaName=deletable.name, user=user)

@app.route('/formula/<int:formula_id>/view/', methods=['GET'])
def viewFormula(formula_id):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    formula = Formula.query.filter_by(id=formula_id).one()

    return render_template('formula_templates/view_formula.html', formula_id=formula_id, formula=formula, user=user)
