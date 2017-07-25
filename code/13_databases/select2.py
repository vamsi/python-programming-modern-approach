import sqlite3
conn = sqlite3.connect('movies.db')
c = conn.cursor()
query = c.execute("SELECT * FROM movies WHERE studio='Pixar';")
for row in query:
    print(row)
