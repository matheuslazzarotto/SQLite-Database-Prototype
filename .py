lista = []
import csv

with open("Login.csv","r") as f:

        leitor = csv.DictReader(f)
        dic = {l["email"]:l["senha"] for l in leitor}
print(dic)