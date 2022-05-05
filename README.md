# SQLite-Database-Prototype

a prototype that I'm working on for my uni project, which consists in using Python and SQLite to prototype a database that will store variables that are used in the calculation of a landslide.

'eureka.py' is the main application. it refers to any db and tables created at 'table_creator' and to any functions in 'functions.py'. currently you can [1] show all lines, [2] delete a line, [3] add a line, [4] fetch a specific line and [5] fetch a value inside a specific line.

'table_creator.py' as you can probably guess creates a table. but it also creates the db that will store the table (in this case, 'landslide_database.db'. you can mess with the parameters and make new tables (or even new databases).

'functions.py' is where all functions are stored.

shout-out to freeCodeCamp, whose 'SQLite Databases With Python' course was extremely helpful. many thanks to some friends as well (Aleixo, Adolfo, Isaac and Erick)
