import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''update attendance set name='akshay' where g_id=2216102'''
conn.execute(query)
print(conn.total_changes)
conn.commit()
conn.close()