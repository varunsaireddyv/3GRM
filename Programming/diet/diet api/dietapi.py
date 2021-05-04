from flask import Flask, request
from flask_restful import Api, Resource
import sqlite3
import json

connection = sqlite3.connect('/home/rajesh/Desktop/3grmvarun/3GRM/Programming/diet/DietDatabase.db')
cursor= connection.cursor()
cursor.execute('SELECT * FROM UserDataDiseseas')    
fetch=cursor.fetchall()

json_convert=json.dumps(fetch)


connection.commit()



app= Flask(__name__)
api=Api(app)

class getuserdata(Resource):
    def get(self):
        return{'data' : json_convert }

api.add_resource(getuserdata, "/getuserdata/<string:>")


if __name__ == "__main__":
    app.run(debug=True)