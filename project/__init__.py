"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)

import home
import formulas.formula_views
import login.login_view
import user.user_creator_menu