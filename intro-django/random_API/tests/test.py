import pandas, sqlite3

def populate_db():
    '''Populate the database with the given info'''
    data = pandas.read_csv('flask-site/countries.txt', sep='|', quotechar="'", names=['name', 'capital', 'currency'], engine='python')
    connection = sqlite3.connect('flask-site/countries.db')
    cursor = connection.cursor()
    try:
        data.to_sql('country_info', connection, index=False)
    except:
        query = cursor.execute('select capital from country_info where name = "Mexico"')
        print(query.fetchall())
    connection.close()

populate_db()