import sqlite3
conn = sqlite3.connect('test.db')
c=conn.cursor()

# c.execute('''CREATE TABLE test (
#     first text
#     last text
#     )''')

t = c.execute('''CREATE TABLE DietData (firstName text, lastName text)''')

x = c.execute('''select * from DietData''')
print(x)