import csv
from tkinter import * #type: ignore

lista = []

def delete_popUp4():
    popUp4.destroy()

def delete_popUp3():
    popUp3.destroy()

def delete_popUp2():
    popUp2.destroy()
    janelaLog.destroy()
    janela.destroy()
    import functions
    import eureka

def login_sucess():

    global popUp2

    popUp2 = Toplevel(janela)
    popUp2.title("Sucesso")
    popUp2.geometry("150x100")
    Label(popUp2,text = "O seu Login foi um sucesso!").pack()
    Button(popUp2,text= "OK",command = delete_popUp2).pack()

def password_not_recognised():

    global popUp3

    popUp3 = Toplevel(janela)
    popUp3.title("Error")
    popUp3.geometry("150x100")
    Label(popUp3,text = "Senha e/ou email invalidos").pack()
    Button(popUp3,text= "OK",command = delete_popUp3).pack()

def user_not_found():
        
    global popUp4

    popUp4 = Toplevel(janela)
    popUp4.title("Error")
    popUp4.geometry("150x100")
    Label(popUp4,text = "Senhas e/ou email invalidos").pack()
    Button(popUp4,text= "OK",command = delete_popUp4).pack()

def register_verify():
    global username_info
    global password_info
    username_info = email.get()
    password_info = password.get()

    with open("Login.csv",mode = 'r') as g:
        reader2 = csv.reader(g)
        global conta_existente
        conta_existente = 0
    
        for row in reader2:
            if row == [username_info]:
                conta_existente += 1

            if conta_existente == 1:
                erro = Label(popUp,text = "Email ja foi utilizado!",fg = "red",font = ("calibri",11))
                erro.pack()
                user_entry.delete(0,END)
                password_entry.delete(0,END)
                break
    

def register_user():

    username_info = lista.append(email.get())
    password_info = lista.append(password.get())

    register_verify()

    if conta_existente == 0:
        with open('Login.csv','a') as f:
            virg = ','.join(lista)
            f.writelines(virg + "\n")
        Label(popUp,text = "Registrado com sucesso!",fg = "green",font = ("calibri",11)).pack()
        
def log_verify():

    global username1
    global password1

    username1 = StringVar()
    password1 = StringVar()
    username1 = username_verify.get()
    password1 = password_verify.get()

    userLog_entry.delete(0,END)
    passwordLog_entry.delete(0,END)

    with open("Login.csv",mode = "r") as f:
        reader = csv.reader(f)
        existe = 0
        for row in reader:
            if row == [username1,password1]:
                existe += 1
                login_sucess()
            
        if existe == 0:
            user_not_found()
            
def register():
    global popUp
    popUp = Toplevel(janela)
    popUp.title("Register")
    popUp.geometry("300x250")

    global email
    global password
    global user_entry
    global password_entry

    email = StringVar()
    password = StringVar()
    
    Label(popUp,text = "Por favor preencha os campos requisitados: ").pack()
    Label(popUp,text = "").pack()
    Label(popUp,text = "Email * ").pack()
    user_entry = Entry(popUp,width = 35,textvariable = email)
    user_entry.pack()
    Label(popUp,text = "Senha * ").pack()
    password_entry = Entry(popUp, width = 35,textvariable = password,show = "*")
    password_entry.pack()
    Label(popUp,text = "").pack()
    Button(popUp,text = "Registrar",width = 10,height=1,command = register_user).pack()

def login():
    global janelaLog

    janelaLog = Toplevel(janela)
    janelaLog.title("Login")
    janelaLog.geometry("300x250")
    Label(janelaLog,text = "Por favor insira os campos abaixo: ").pack()
    Label(janelaLog,text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global passwordLog_entry
    global userLog_entry

    Label(janelaLog,text = "Email * ").pack()
    userLog_entry = Entry(janelaLog,width =35,textvariable = username_verify)
    userLog_entry.pack()

    Label(janelaLog,text = "").pack()

    Label(janelaLog,text = "Senha * ").pack()
    passwordLog_entry = Entry(janelaLog,width = 35,textvariable = password_verify,show = "*")
    passwordLog_entry.pack()

    Label(janelaLog,text = "").pack()
    Button(janelaLog,text = "Login", width= 10, height= 1, command = log_verify).pack()

def janelaPrincipal():
    global janela
    janela = Tk()
    janela.geometry("300x250")
    janela.title("Login")
    Label(text = "Bem vindo ao banco de dados eureka!",width = "300",height = "2",font = ("Lato",13)).pack()
    Label(text = "").pack()
    Button(text = "Login",height = "2",width = "35",command = login).pack()
    Label(text = "").pack()
    Button(text = "Registre-se",height = "2",width = "35",command = register).pack()
    Label(text = "").pack()

    janela.mainloop()

janelaPrincipal()
