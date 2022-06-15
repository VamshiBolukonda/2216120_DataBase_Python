import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("drop table attendance")
conn.commit()
conn.close()