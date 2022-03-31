from flask import Blueprint, render_template

# Make this a Blueprint
temperature = Blueprint('temperature', __name__)

# URL for converting temperatures
@temperature.route('/convert')
def convert():
    '''Convert temperature value between Celcius and Fahrenheit'''
    return render_template('temperature.html')