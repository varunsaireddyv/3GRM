import sqlite3

connection = sqlite3.connect('poop.db')
cursor= connection.cursor()
x=cursor.execute('CREATE TABLE UserDataDiet (first text)')
y=cursor.execute("INSERT INTO UserDataDiet VALUES ('corey')")

connection.commit
