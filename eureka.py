import functions
import sqlite3

while(True):
    print()
    print("Bem vindo ao banco de dados EUREKA, essas são suas opções:")
    print("1 - mostrar as encostas presentes no banco de dados;")
    print("2 - adicionar uma encosta ao banco de dados;")
    print("3 - Deletar uma encosta do banco de dados;")
    print("4 - visualizar uma encosta em especifica;")
    print("5 - visualizar uma varivel de uma encosta")
    print("0 - End program.")
    print()
    value = float(input("Por favor insira uma opção: "))
    
    if value == 1:
        functions.show_all()
        continue

    elif value == 2:
        slope_name= input("Por favor insira o nome da encosta: ")
        slope_lat= input("Insira a latitude da encosta: ")
        slope_long= input("Insira a longitude: ")
        declivity= input("Insira a declividade: ")
        houses_per_square_meter= input("Insira a quantidade de casas por metro quadrado: ")
        trees_per_square_meter= input("Insira a quantidade de arvores por metro quadrado: ")
        liquid_proximity= input("Por favor insira a proximidade de superfícies líquidas: ")
        soil_umidity= input("insira o coeficiente de umidade do solo: ")

        functions.add_one(slope_name,slope_lat,slope_long,declivity,houses_per_square_meter,
        trees_per_square_meter,liquid_proximity,soil_umidity)

        continue

    elif value == 3:
        id = str(input("Insira o id da encosta que voce deseja remover: "))
        functions.delete_one(id)
        continue
    
    elif value == 4:
        id = str(input("Insira o id da encosta que voce deseja ver: "))
        functions.general_fetch(id)
        continue

    elif value == 5:
        id = (input("\nInsira o id da encosta que voce deseja ver: "))
        print("\n\nInsira abaixo qual das opções você deseja visualizar.\n\nopções: \n\n1 - nome da encosta;")
        print("2 - latitude ;\n3 - longitude;\n4 - declividade;\n5 - casas por metro quadrado;")
        print("6 - arvores por metro quadrado,\n7 - proximidades de liquidos,\n8 - umidade do solo.")

        op = int(input("insira aqui: "))
        functions.specific_fetch(id,op)
        continue
    
    else:
        break

