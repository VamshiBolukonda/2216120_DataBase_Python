import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''
     alter table participants add column addr text not null
'''
conn.execute(query)
conn.commit()
conn.close()