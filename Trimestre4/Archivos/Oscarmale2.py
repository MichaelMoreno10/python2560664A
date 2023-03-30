from Clase import *
import csv
listaapre=[]
with open ("archivos/oscar_age_male.csv","r") as oscarhombre:
    csvReader=csv.reader(oscarhombre)
    for y in csvReader:
        ob=Persona2(y[0],y[1],y[2],y[3],y[4])
        listaapre.append(ob)

print(listaapre)        

for apre in listaapre:
    print(apre.pelicula())