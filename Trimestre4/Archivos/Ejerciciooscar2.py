from Clase import *
import csv
listaapre=[]
with open ("archivos/oscar_age_female.csv","r") as oscarmujer:
    csvReader=csv.reader(oscarmujer)
    for y in csvReader:
        ob=Persona(y[0],y[1],y[2],y[3],y[4])
        listaapre.append(ob)

print(listaapre)        

for apre in listaapre:
    print(apre.pelicula())
    