from flask import Flask, render_template, request, redirect, flash, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.make_database import Base, Formula, User
app = Flask(__name__)

engine = create_engine('sqlite:///database/formula.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/formulas')
def printFormulas():
    formulas = session.query(Formula).all()
    return render_template('layout.html', formulas=formulas)


@app.route('/restaurant/new/formula', methods=['GET', 'POST'])
def newFormula():
    if request.method == 'POST':
        new = Formula(name=request.form['name'], description=request.form['description'])
        session.add(new)
        session.commit()
        flash(new.name + " was created")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('newFormula.html')

# Task 2: Create route for editMenuItem function here


@app.route('/restaurant/<int:formula_id>/edit/', methods=['GET', 'POST'])
def editFormula(formula_id):
    editable = session.query(Formula).filter_by(id=formula_id).one()
    if request.method == 'POST':
        editable.description = request.form['description']
        session.add(editable)
        session.commit()
        flash(editable.name + " was updated")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('editFormula.html', formula_id=formula_id, formulaName=editable.name, formulaDescription=editable.description)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/restaurant/<int:formula_id>/delete/', methods=['GET', 'POST'])
def deleteFormula(formula_id):
    deletable = session.query(Formula).filter_by(id=formula_id).one()
    if request.method == 'POST':
        session.delete(deletable)
        session.commit()
        flash(deletable.name + " was deleted")
        return redirect(url_for('printFormulas'))
    else:
        return render_template('deleteFormula.html', formula_id=formula_id, formulaName=deletable.name)


if __name__ == '__main__':
    app.secret_key ='super_secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)