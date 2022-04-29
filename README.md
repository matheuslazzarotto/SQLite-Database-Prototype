# SQLite-Database-Prototype

a prototype that I'm working on for my uni project, which consists in using Python and SQLite to prototype a database that will store variables that are used in the calculation of a landslide.

'eureka.py' is the main application. it refers to any db and tables created at 'table_creator' and to any functions in 'functions.py'. currently you can show all lines, delete a line, add a line and fetch a particular value from a line.

'table_creator.py' as you can probably guess creates a table. but it also creates the db that will store the table (in this case, 'landslide_database.db'. you can mess with the parameters and make new tables (or even new databases).

'functions.py' is where all functions are stored.
