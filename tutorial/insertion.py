import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

print("Command executed succesfully.")
#commit our command
conn.commit()

#close connection
conn.close()