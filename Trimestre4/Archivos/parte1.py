from aprendiz import *  #Se crea una importacion de la clase aprendiz
from curso import *     #Se crea una importacion de la clase aprendiz



with open('Archivos/aprendices.txt','r') as flujo: #Se utiliza un metodo para decirle donde esta nuestro archivo con la variable local donde se guarda todo lo del archivo
    datos=flujo.read()    #Se crea otra variable que va almacenar la variable local con un metodo para visualizar 
    print(datos)   #se imprime la ultima variable creada 
    #flujo.write('2560664,maria,123')
aprendices=[]     #se crea una variable que va hacer equivalente a una lista vacia
with open('Archivos/aprendices.txt','r') as flujo:  #se utiliza un metodo para decirle donde esta nuestro archivo con la variable local donde se guarda todo lo del archivo
    for linea in flujo:  #Se crea un for para recorrer una nueva variable en la variable local
        #print(linea)
        aprendices.append(linea.rsplit())  #a la lista creada se le va a agregar la variable que recorre el for y se utiliza el metodo para quitar el \n

datosxlinea=[]   #Se crea otra variable que va hacer otra lista vacia
for aprendiz in aprendices:  #se crea un for para recorrer una nueva variable en la lista que contiene una cadena entera dentro de una lista, y esa lista esta dentro de otra lista
    datosxlinea.append(aprendiz[0].split(',')) #la lista vacia se le agrega lo que contiene la variable "aprendiz" en el indice 0 y se le coloca el metodo para que separe donde haya una coma

#print(ob.getNombre())

print(datosxlinea)  #Se imprime la variable "datosxlinea", que es una lista

listaDeObjetos=[]  #se crea otra variable que es una lista vacia 
for apr in datosxlinea:   #se crea un for para recorrer una nueva variable que recorre la variable "datosxlinea"
     f=apr[0] #se crea una variable que almacena lo que tiene la variable"apr" en la posicion 0
     n=apr[1]  #se crea una variable que almacena lo que tiene la variable"apr" en la posicion 1
     d=apr[2] #se crea una variable que almacena lo que tiene la variable"apr" en la posicion 2
     ob=Aprendiz(f,n,d)  #Se crea una variable para llamar la clase "Aprendiz" pasandole los parametros
     print(ob)   #Se imprime la variable
     listaDeObjetos.append(ob)    #Se agrega lo que contenga la variable "ob" a la lista vacia

for xx in listaDeObjetos:  #Se crea un for para recorrer la variable "listadeobjetos"
    print(xx.getNombre())   #Se imprime el metodo "getnombre"
    print(xx.getDocumento())   #se imprime el metodo "getdocumento"