import sqlite3


def show_all():
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.execute ("SELECT rowid, * FROM variables")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

def add_one(slope_name,slope_lat,slope_long,declivity,houses_per_square_meter,
trees_per_square_meter,liquid_proximity,soil_umidity):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO variables VALUES (?,?,?,?,?,?,?,?)", (slope_name,slope_lat,
    slope_long,declivity,houses_per_square_meter,
    trees_per_square_meter,liquid_proximity,soil_umidity))
    conn.commit()
    conn.close()

def delete_one(id):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.execute("DELETE from variables WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

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

#def specific_fetch(rowid,columnid):
    # conn = sqlite3.connect('landslide_database.db')
    # c = conn.cursor()
    # c.execute("SELECT * from variables WHERE rowid = (?)",rowid)
    # c.execute("SELECT * from variables WHERE columnid = (?)",columnid)
    # c.fetchone()
    # print()
    # conn.comit()
    # conn.close()

#def create_index(https://www.sqlite.org/lang_createindex.html)