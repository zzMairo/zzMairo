import random
import csv
#import pandas as pd
#funciona en colab, no funciona aca porque no instale libreria pandas con el pip install pandas
num = 0
numero_500=[]
tup = ("indice","numero","numero random","factorial")
numero_500.append(tup)

def factorial(numero):
    for i in range(1,501):
        numero_r = random.randint(-100,100)
        #print(numero_r)
        num= numero*numero_r
    
        #print(f"gg{num}")
        tup = (i,numero,numero_r,num)
        numero_500.append(tup)

    #print(numero_500)
    with open("factorial.csv", "w", newline="\n") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for row in numero_500:
            writer.writerow(row)

    #pd.read_csv('contactos.csv').to_excel('factorial.xlsx',index= False)

factorial(int(input("ingrese un numero: ")))

with open("factorial.csv", "r", newline="\n") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    for row in lector:
        print(row)
