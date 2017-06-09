import sqlite3
conn = sqlite3.connect('movies.db')
c = conn.cursor()
query = c.execute("SELECT * FROM movies;")
print("Movies Database")
for row in query:
    for column in row:
        print(column)
    print("---")
