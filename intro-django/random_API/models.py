from . import db

# Account Model
class Account(db.Model):
    # Define the columns (primary key required)
    account_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), unique=True, nullable=False)
    last_name = db.Column(db.String(25), unique=True, nullable=False)
    balance = db.Column(db.Float, unique=True, nullable=False)
