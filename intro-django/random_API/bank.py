from flask import Blueprint, render_template

# Make this a Blueprint
bank = Blueprint('bank', __name__)

# Landing page for the bank app
@bank.route('/')
def bank_page():
    '''Main page of the banking app'''
    return render_template('bank.html')