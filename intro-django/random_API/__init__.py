from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Instantiate the database object
db = SQLAlchemy()

def build_app():
    '''Create the app object for the site.'''
    # Instantiate and configure the app object
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///random_API.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Import the Models
    from .models import Account

    # Build the database
    build_database(app)

    # Import the Blueprints
    from .views import views
    from .countries import countries
    from .temperature import temperature
    from .bank import bank

    # Register the Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(countries, url_prefix='/countries')
    app.register_blueprint(temperature, url_prefix='/temperature')
    app.register_blueprint(bank, url_prefix='/bank')

    return app

def build_database(app):
    '''Create the database if it doesn't exist'''
    # Check if the database already exists before trying to build it
    if not path.exists('random_API/random_API.db'):
        db.create_all(app=app)