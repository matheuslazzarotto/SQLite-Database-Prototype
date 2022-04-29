import sqlite3
conn = sqlite3.connect('variables.db')
c = conn.cursor()
c.execute("""CREATE TABLE variables (
        slope_name text,
        slope_long float,
        slope_lat float,
        declivity float,
        houses_per_square_meter float,
        trees_per_square_meter float,
        liquid_proximity float,
        soil_umidity float,
        )""")
conn.commit()
conn.close()