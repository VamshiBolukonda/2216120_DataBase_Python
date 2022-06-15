import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
'''
    query -> pragma table_info('table_name')
'''
str=conn.execute("pragma table_info('attendance')")
print(str)
for i in  str:
    print(i)