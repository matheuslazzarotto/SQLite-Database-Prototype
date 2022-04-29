import sqlite3

#query the database and return all records
def show_all():
    #connect to db
    conn = sqlite3.connect('landslide_database.db')
    #create a cursor
    c = conn.cursor()
    #query the db
    c.execute ("SELECT rowid, * FROM variables")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

#add new record to the db
def add_one(slope_name,slope_lat,slope_long,declivity,houses_per_square_meter,
trees_per_square_meter,liquid_proximity,soil_umidity):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO variables VALUES (?,?,?,?,?,?,?,?)", (slope_name,slope_lat,slope_long,declivity,houses_per_square_meter,
    trees_per_square_meter,liquid_proximity,soil_umidity))
    conn.commit()
    conn.close()

#deleting a record of the db
def delete_one(id):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.execute("DELETE from variables WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

#add more than one record to the list
def add_many(list):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.executemany("INSERT INTO variables VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()
    
def fetch_one(id):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.execute("SELECT * from variables WHERE rowid = (?)", id)
    row = c.fetchone()
    print(row)
    conn.commit()
    conn.close()