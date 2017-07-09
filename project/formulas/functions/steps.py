from project.database.formula_chemicals.models import Instruction
from flask_server import db
import logging

def newSteps(f_key, step_array):

    for i in step_array:
        logging.warn(i)
        new = Instruction(
            formula_key=f_key,
            step_number=i,
            step=step_array[int(i)]
        )

        logging.warn(new)
        db.session.add(new)
        db.session.commit()

    return
