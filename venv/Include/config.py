import sqlite3 as db

d = db.connect('animals.db')
c = d.cursor()
c.execute('SELECT * FROM animals')
print(c.fetchall())
d.commit()
d.close()