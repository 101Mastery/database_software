from project.database.formula_chemicals.models import Instruction, Chemical, Ingredient
from flask_server import db
import uuid
import logging


def new_ingredient(f_key, step_key, chemical_array, amount_array, unit_array):
    if len(chemical_array) != 0:
        for n in range(0, len(chemical_array)):
            newI = Ingredient(
                formula_key=f_key,
                step_key=step_key,
                ingredient_name=chemical_array[n].name,
                ingredient_key=chemical_array[n].key,
                amount=amount_array[n],
                unit=unit_array[n]
            )
            db.session.add(newI)

    return


def new_steps(f_key, step, key, number):

    newS = Instruction(
        formula_key=f_key,
        step_number=number,
        step=step,
        key=key
    )

    db.session.add(newS)

    return

