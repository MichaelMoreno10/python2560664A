import random
cont=0
posicion=""
rango=random.randint(10,25)
vector=[round(random.random()*100)for i in range(rango)]
print(vector)

numero=int(input("elija el numero:"))
for i in range(rango):
    if numero==vector[i]:
        posicion+=str(i)+""
        cont+=1
if cont==0:
    vector.append(numero)
    print("e numero se agrego al final de la lista")
    print(vector)
else:
    if cont==1:
        print("el numero de la ista",numero, "esta1 vez y en la posicion:",posicion) 
        print("el numero de a lista",numero,"esta",cont,"veces y esta en la posicion",posicion)