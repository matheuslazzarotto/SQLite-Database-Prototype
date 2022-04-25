import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

#DATATYPES:
    #NULL
    #INTEGER
    #REAL
    #TEXT
    #BLOB

#commit our command
conn.commit()

#close connection
conn.close()