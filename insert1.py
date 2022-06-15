import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into attendance values(2216120,'vamshi',99,'HNK')")
conn.execute("insert into attendance  values(2216103,'ram charan',98,'KZP')")
conn.execute("insert into attendance  values(2216102,'akshay rao',97,'WGL')")
conn.commit()
conn.close()