from project.database.formula_chemicals.models import Instruction
from flask_server import db
import logging

def newSteps(f_key, step_array):

    for i in range(0, len(step_array)):
        logging.warn(i)
        new = Instruction(
            formula_key=f_key,
            step_number=i,
            step=step_array[i]
        )

        logging.warn(new)
        db.session.add(new)
        db.session.commit()

    return
