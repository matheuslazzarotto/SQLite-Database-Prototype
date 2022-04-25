from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Welcome to the Database!\n\n\n\n")
myLabel2 = Label(root, text="Created by Grupo Eureka")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)

root.mainloop()
