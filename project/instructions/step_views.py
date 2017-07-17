from flask import render_template, request, redirect, flash, url_for
from project import app
from project.database.formula_chemicals.models import Formula, Chemical, Ingredient, Instruction
from project.database.users.models import User

@app.route('/formula/<int:formula_id>/<int:step_number>/', methods=['GET'])
def print_step(formula_id, step_number):

    try:
        user = User.query.filter_by(user_name=request.cookies.get('UserCookie')).one()
    except:
        return redirect(url_for('login'))

    formula = Formula.query.filter_by(id=formula_id).one()
    step = Instruction.query.filter_by(formula_key=formula.key, step_number=int(step_number)).one()
    ingredients = Ingredient.query.filter_by(formula_key=formula.key, step_key=step.key)

    try:
        next_step = Instruction.query.filter_by(formula_key=formula.key, step_number=int(step_number)+1).one()
        next_step_number =next_step.step_number
        max_step_number = False
    except:
        max_step_number = True

    return render_template('instruction_templates/step.html',
                           formula_id=formula_id,
                           formula=formula,
                           user=user,
                           ingredients=ingredients,
                           step=step,
                           max_step_number=max_step_number)
