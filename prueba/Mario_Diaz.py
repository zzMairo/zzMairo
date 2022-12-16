import csv
suma = 0
lista = []

with open("cotizacion.csv", "r", newline="\n") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    next(lector, None)  # para que no lea la cabezera
    ab = True
    # for i in range(1,6):
      # print(i)
    for row in lector:
        if ab == True:
                primer_num = row[1]
                print(f"---{primer_num}---")
                mayor = primer_num 
                menor = primer_num
                ab = False
        elif menor > row[1]:
                menor = row[1]

        elif mayor< row[1]:
            mayor=row[1]
    
        suma = suma + row[1]

    print(f"el menor de columna 1 es : {menor}")
    print(f"el mayor de columna 1 es : {mayor}")
    print(f"la  suma de columna 1 es : {suma}")

"""with open("cotizacion.csv", "r", newline="\n") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    next(lector, None)  # para que no lea la cabezera
    ab = True
    for row in lector:
        #print("ee")
        print(row[0])"""



"""        for Final in lector:
            print(Final)
            if ab== True:
                primer_num = Final[1]
                print(f"---{primer_num}---")
                ab = False
            elif primer_num > Final[1]:
                primer_num = Final[1]
        print(f"el menor de columna 1 es : {primer_num}")
"""
        
        
"""


        if i==1:
            columna1 = primer_num
        elif i ==2:
            columna2 = primer_num
        elif i ==3:
            columna3 = primer_num
        elif i ==4:
            columna4 = primer_num
        elif i ==5:
            columna5 = primer_num
    fila = (columna1,columna2,columna3,columna4,columna5)"""


"""contactos = [
  ("", "minimo", "maximo","media"),	 # <- La primera tupla es CABECERA del csv
  ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
  ("Javier", "Analista de datos", "javier@ejemplo.com"),
  ("Marta", "Experta en Python", "marta@ejemplo.com")
]
with open("contactos.csv", "w", newline="\n") as csvfile:
  writer = csv.writer(csvfile, delimiter=",")
  for contacto in contactos:
      writer.writerow(contacto)"""


# final,minimo,maximo,volumen,efectivo
#Nombre, Final, Máximo, Mínimo, Volumen, Efectivo
