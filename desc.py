import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
'''
    query -> pragma table_info('tablename')
'''
str=conn.execute("pragma table_info('participants')")
print(str)
for i in  str:
    print(i)