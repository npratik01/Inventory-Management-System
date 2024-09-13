import sqlite3
def create_db():
    con = sqlite3.connect(database='ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS member(memid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, pass text, utype text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    con.commit()
    

create_db()