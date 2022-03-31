from flask import Blueprint, render_template
from random import randint

# Make this a Blueprint
views = Blueprint('views', __name__)

# Route for landing page
@views.route('/')
def lucky():
    '''Landing page that shows today's lucky numbers'''
    return render_template('home.html', lucky_nums = [randint(1, 60) for i in range(6)])