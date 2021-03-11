import sqlite3

connection = sqlite3.connect('testdb.db')
cursor= connection.cursor()
cursor.execute('CREATE TABLE UserDataDiet (first text, last text, mail text)')




connection.commit()
