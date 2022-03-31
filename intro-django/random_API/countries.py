import sqlite3, pandas
from flask import Blueprint, render_template

# Make this a Blueprint
countries = Blueprint('countries', __name__)

# Populate the database from the text file
def populate_db():
    '''Populate the database with the given info'''
    data = pandas.read_csv('random_API/static/countries.txt', sep='|', quotechar="'", names=['name', 'capital', 'currency'], engine='python')
    connection = sqlite3.connect('random_API/countries.db')
    cursor = connection.cursor()
    try:
        data.to_sql('country_info', connection, index=False)
    except:
        pass
    connection.close()

# Query info from the database
def query_db(country: str, data: str):
    '''Pull data from the database'''
    connection = sqlite3.connect('random_API/countries.db')
    cursor = connection.cursor()
    query = cursor.execute(f'select name, {data} from country_info where name is "{country}";').fetchone()
    connection.close()
    return query

# Page that shows a list of NATO Countries
@countries.route('/nato')
def nato():
    '''An unordered list of NATO Countries'''
    with open('random_API/static/nato.txt', 'r') as f:
        countries = [country.split(',')[0] for country in f.readlines()]
    return render_template('nato.html', countries = countries)

# URL for querying the currency of a given country
@countries.route('/currency/<country>')
def get_currency(country):
    '''API Request handler for currencies of countries'''
    populate_db()
    data = query_db(country, 'currency')
    return f'The currency of {data[0]} is {data[1]}.'

# URL for querying the capital of a given country
@countries.route('/capital/<country>')
def get_capital(country):
    '''API Request handler for capitals of countries'''
    populate_db()
    data = query_db(country, 'capital')
    return f'The capital of {data[0]} is {data[1]}.'
