import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

many_customers =    [
                    ('Wes', 'Brown', 'wes@brown.com'),
                    ('Steph', 'Kuewva', 'steph@kuewa.com'),
                    ('Dan', 'Pas', 'dan@pas.com')
                    ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

print("Command executed succesfully.")
#commit our command
conn.commit()

#close connection
conn.close()