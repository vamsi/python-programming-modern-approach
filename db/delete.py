import sqlite3
conn = sqlite3.connect('movies.db')
c = conn.cursor()
query = c.execute("DELETE From movies WHERE movie='Frozen';")
conn.commit()
print("Record Successfully Deleted")
