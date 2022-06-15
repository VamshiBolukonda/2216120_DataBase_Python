import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''update participants set name='yashwanth' where g_id=2216101'''
conn.execute(query)
print(conn.total_changes)
conn.commit()
conn.close()