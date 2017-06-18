"""
The flask application package.
"""

from flask import Flask


app = Flask(__name__)


import project.home
import project.formulas.formula_views
import project.login.login_view
import project.user.user_creator_menu
