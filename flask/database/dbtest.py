import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()    
cur.execute("SELECT * FROM fruits")
rows = cur.fetchall()
print(rows)
