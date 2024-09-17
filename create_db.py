import sqlite3

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    
    # Create member table
    cur.execute("""
<<<<<<< HEAD
        CREATE TABLE IF NOT EXISTS member (
            memid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            pass TEXT,
            utype TEXT
        )
    """)
=======
            CREATE TABLE IF NOT EXISTS product(
                Invoice_number INTEGER PRIMARY KEY AUTOINCREMENT, 
                [Product Name] TEXT, 
                [Invoice date] TEXT, 
                Price INTEGER, 
                qty REAL,
                [Total Invoice Amount] TEXT, 
                [Supplier Name] TEXT, 
                [Vendor MO NO] TEXT, 
                [Email of vendor] TEXT, 
                [R Student Name] TEXT, 
                [R Std Mo No] TEXT, 
                [Current position] TEXT, 
                [Current Mo No] TEXT
                
            )
        """)
>>>>>>> 35ba6a2fcd2a8a523a1b5ee14c47a87ee9061ae9
    con.commit()
    
    # Create supplier table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS supplier (
            invoice INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            desc TEXT
        )
    """)
    con.commit()
    
    # Create product table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product (
            Invoice_number INTEGER PRIMARY KEY AUTOINCREMENT,
            [Product Name] TEXT,
            [Invoice date] TEXT,
            Price INTEGER,
            qty REAL,
            [Total Invoice Amount] TEXT,
            [Supplier Name] TEXT,
            [Vendor MO NO] TEXT,
            [Email of vendor] TEXT,
            [R Student Name] TEXT,
            [R Std Mo No] TEXT,
            [Current position] TEXT,
            [Current Mo No] TEXT
        )
    """)
    con.commit()
    
    con.close()

create_db()
