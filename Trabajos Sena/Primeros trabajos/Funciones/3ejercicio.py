#1 de listas 
import random
def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randit(10.25))]
    return lista

lista=llenar_lista(list)
lista.sort()
rango=len(lista)

def promedio(lista):
    suma=0
    for i in range(rango):
        suma+=lista[i]
    promedio=suma//rango
    return promedio

print("el rango de la list es",rango) 
print("los valores de la lista son", lista)
print("el promedio de los valores es", promedio(lista))

for n in lista:
    if n<promedio(lista):
        print("el numero",n,"es menor al promedio")
    elif n>promedio(lista):
        print("el numero",n,"es mayor del promedio")
    elif n==promedio(lista):
        print("el numero",n,"es igual al promedio")    
