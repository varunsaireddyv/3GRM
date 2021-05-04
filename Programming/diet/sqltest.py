import sqlite3
import json

connection = sqlite3.connect('/home/rajesh/Desktop/3grmvarun/3GRM/Programming/diet/DietDatabase.db')
cursor= connection.cursor()
cursor.execute('SELECT * FROM UserDataDiseseas')    
fetch=cursor.fetchall()

json_convert=json.dumps(fetch)

print(json_convert)

connection.commit()
