from project.database.formula_chemicals.models import Instruction, Chemical, Ingredient
from flask_server import db
import uuid
import logging


def new_ingredient(f_key, step_key, chemical_key, amount, unit):

    new = Ingredient(
        formula_key=f_key,
        step_key=step_key,
        ingredient_key=chemical_key,
        amount=amount,
        unit=unit
    )

    db.session.add(new)
    db.session.commit()

    return


def new_steps(f_key, step_array, ingredients, ingredient_count_array, amount_array, unit_array):

    x=0
    for i in range(0, len(step_array)):
        new = Instruction(
            formula_key=f_key,
            step_number=i,
            step=step_array[i],
            key=uuid.uuid4()
        )

        db.session.add(new)
        db.session.commit()
        logging.warn(new.key)

        for n in range(x, int(ingredient_count_array[i])+x):
            chemical = ingredients[n]
            new_ingredient(f_key, new.key, chemical, amount_array[n], unit_array[n])
            x=x+1

    return
