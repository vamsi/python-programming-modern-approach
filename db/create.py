import sqlite3
conn = sqlite3.connect('movies.db')
c = conn.cursor()

c.execute(
    """
CREATE TABLE movies (
id INTEGER,
movie TEXT,
year TEXT,
rating REAL,
studio TEXT
)
""")
conn.close()
# Close database
