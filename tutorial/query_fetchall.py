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

#query the database
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)

items = c.fetchall()
print("NAME " + "\t\tEMAIL")
print("-------" + "\t\t-------")

for item in items:
    print(item[0] + " " + item[1] + "\t" + item[2])


#commit our command
conn.commit()

#close connection
conn.close()