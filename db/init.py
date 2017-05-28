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
dataset = ((1, "Up", 2009, 8.3, "Pixar"),
           (2, "Toy story", 1995, 8.3, "Pixar"),
           (3, "Finding Nemo", 2003, 8.1, "Pixar"),
           (4, "Zootopia", 2016, 8.1, "Disney"),
           (5, "Moana", 2016, 7.7, "Disney"),
           (6, "Despicable Me", 2010, 7.7, "Illumination"),
           (7, "Frozen", 2013, 7.5, "Disney"))

for item in dataset:
    # Write data to database
    c.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", item)
    conn.commit()
conn.close()  # Close database
