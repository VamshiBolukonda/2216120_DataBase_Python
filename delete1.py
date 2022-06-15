import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("delete from attendance where study='KZP'")
print(conn.total_changes)
conn.commit()
conn.close()