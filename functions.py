import sqlite3

#query the database and return all records
def show_all():
    #connect to db
    conn = sqlite3.connect('customer.db')
    #create a cursor
    c = conn.cursor()
    #query the db
    c.execute ("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

#add new record to the db
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first,last,email))
    conn.commit()
    conn.close()

#deleting a record of the db
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

#add more than one record to the list
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()
    
def fetch_one(id, op):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    if op == 1:
        c.execute("SELECT first_name from customers WHERE rowid = (?)", id)
    elif op == 2:
        c.execute("SELECT last_name from customers WHERE rowid = (?)", id)
    else:
        c.execute("SELECT email from customers WHERE rowid = (?)", id)
    row = c.fetchone()
    print(row)
    conn.commit()
    conn.close()
