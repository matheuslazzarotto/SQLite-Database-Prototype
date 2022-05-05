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
    
def general_fetch(id):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    c.execute("SELECT * from variables WHERE rowid = (?)", id)
    row = c.fetchone()
    print(row)
    conn.commit()
    conn.close()

def specific_fetch(id,op):
    conn = sqlite3.connect('landslide_database.db')
    c = conn.cursor()
    if op == 1:
        c.execute("SELECT slope_name from variables WHERE rowid = (?)", id)
    elif op == 2:
        c.execute("SELECT slope_lat from variables WHERE rowid = (?)", id)
    elif op == 3:
        c.execute("SELECT slope_long from variables where rowid = (?)", id)
    elif op == 4:
        c.execute("SELECT declivity from variables where rowid = (?)", id)
    elif op == 5:
        c.execute("SELECT houses_per_square_meter from variables where rowid = (?)", id)
    elif op == 6:
        c.execute("SELECT trees_per_square_meter from variables where rowid = (?)", id)
    elif op == 7:
        c.execute("SELECT liquid_proximity from variables where rowid = (?)", id)
    elif op == 8:
        c.execute("SELECT soil_umidity from variables where rowid = (?)", id)
    else:
        print("error: no such value, please try again.")
    row_c = c.fetchone()
    print("\n",row_c,"\n")
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