import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into participants values(2216120,'vamshi','cseai','Btech','HNK')")
conn.execute("insert into participants values(2216103,'ram charan teja','cseai','Btech','KZP')")
conn.execute("insert into participants values(2216101,'yash','cse','Btech','WGL')")
conn.execute("insert into participants values(2216102,'akshay rao','cse','Btech','KRM')")
conn.commit()
conn.close()