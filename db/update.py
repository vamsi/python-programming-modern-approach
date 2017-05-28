import sqlite3
conn = sqlite3.connect('movies.db')
c = conn.cursor()
query = c.execute("UPDATE movies SET rating=8.7 WHERE movie='Frozen';")
conn.commit()
print("Record Successfully Updated")
