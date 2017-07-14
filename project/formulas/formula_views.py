"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from project import app
from project.database.formula_chemicals.models import Formula, Chemical
from project.database.users.models import User
from flask_server import db
from project.formulas.functions.steps import newSteps


@app.route('/formula')
def printFormulas():

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    formulas = Formula.query.all()
    return render_template('formula_templates/printFormulas.html', formulas=formulas, user=user)


@app.route('/formula/new', methods=['GET', 'POST'])
def newFormula():

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new = Formula(
            name=request.form['name'],
            description=request.form['description'],
            user_key=user.key,
            prep=request.form['prep_instructions'],
            time_rq_days=request.form['time_required_days'],
            time_rq_hr=request.form['time_required_hr'],
            time_rq_min=request.form['time_required_min'],
            beyond_use=request.form['beyond_use'],
            storage=request.form['storage'])

        x = request.form['stepCount']

        try:
            if str(request.form['explosive']) == 'true':
                new.explosive = True
        except:
            new.explosive = False

        try:
            if str(request.form['flammable']) == 'true':
                new.flammable = True
        except:
            new.flammable = False

        try:
            if str(request.form['oxidizer']) == 'true':
                new.oxidizer = True
        except:
            new.flammable = False

        try:
            if str(request.form['corrosive']) == 'true':
                new.corrosive = True
        except:
            new.corrosive = False

        try:
            if str(request.form['toxic']) == 'true':
                new.toxic = True
        except:
            new.toxic = False

        db.session.add(new)
        db.session.commit()

        stepArray=[]

        for i in range(0, int(x)):
            name = 'step_'+str(i)
            stepArray.append(request.form[name])

        newSteps(new.key, stepArray)

        flash(new.name + " was created ")
        return redirect(url_for('printFormulas', user=user))
    else:
        chemicals = Chemical.query.all()
        return render_template('formula_templates/newFormula.html', user=user, chemicals=chemicals)

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
        editable.prep = request.form['prep_instructions']
        editable.time_rq_days = request.form['time_required_days']
        editable.time_rq_hr = request.form['time_required_hr']
        editable.time_rq_min = request.form['time_required_min']
        editable.beyond_use = request.form['beyond_use']
        editable.storage = request.form['storage']

        try:
            if str(request.form['explosive']) == 'true':
                editable.explosive = True
        except:
            editable.explosive = False

        try:
            if str(request.form['flammable']) == 'true':
                editable.flammable = True
        except:
            editable.flammable = False

        try:
            if str(request.form['oxidizer']) == 'true':
                editable.oxidizer = True
        except:
            editable.oxidizer = False

        try:
            if str(request.form['corrosive']) == 'true':
                editable.corrosive = True
        except:
            editable.corrosive = False

        try:
            if str(request.form['toxic']) == 'true':
                editable.toxic = True
        except:
            editable.toxic = False

        db.session.add(editable)
        db.session.commit()
        flash(editable.name + " was updated")
        return redirect(url_for('printFormulas', user=user))
    else:
        return render_template('formula_templates/editFormula.html', formula=editable, user=user, formula_id=formula_id,)

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

