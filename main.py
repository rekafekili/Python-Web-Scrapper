from flask_frozen import Freezer
from assignments.assign09.assign09_flask import app

freezer = Freezer(app)
freezer.freeze()
