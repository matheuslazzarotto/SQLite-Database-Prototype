# SQLite-Database-Prototype

a prototype that me and [@LucasdfRocha](https://github.com/LucasdfRocha) are working on for a uni project, which consists in using Python, Tkinter, and SQLite to prototype a database that will store variables that are used in the calculation of a landslide.

_"loginEureka.py"_ is the app that needs to be run. It also constains the functions responsible for the login and refers to _"eureka.py"_, the database app that runs on terminal when login is successful. all the database functions that _"eureka.py"_ uses are referred to _"functions.py"_.

currently you can:
[1] show all slopes
  when you choose the option [1], you can view all slopes and their variables that are currently at the database.
  
[2] delete a line
  The option [2], delete the slope choosed and EVERY variable inside it.
  
[3] add a line 
  the [3] allows us to create a new line, meaning that a new slope will be added to the database, without the variables.
  
[4] fetch a specific line
  the [4] is to show ALL variables of the choosen slope.
  
[5] fetch a value inside a specific line.
  and the [5] is similar to the [4], but in this case, you choose to see a specfic variable from a specific slope.
  
### to-do:
- index
- sort by fuction
- a less ugly GUI
- alter by line function
- alter by line/row function
- do a csv based register/login system.

shout-out to freeCodeCamp, whose [SQLite Databases With Python](https://www.youtube.com/watch?v=byHcYRpMgI4) course was extremely helpful. many thanks to some friends as well (Aleixo, Adolfo, Isaac and Erick)
