import random 


vector=[]
suma=0
prome=0
cont=0

rango=random.randint(10,25)
for i in range (rango):
    vector.append(round(random.random()*100))
    suma+=vector[i]
    prome=suma//rango
print("El rango de la lista es:",rango)
print("Los valores de la lista son:",vector)
print("El promedio de los valores es:",prome)    

for n in vector:
    if n<prome:
       print("El numero ",n, "es menor al promedio")
    elif n>prome:
        print("el numero ",n, "es mayor al promedio")
    elif n==prome:
        cont+=1
        print("El numero",n,"es igual al promedio")