import random 

tam=int(input("Cuantos numeros"))
vector=[]
contp=0
conti=0
sumapar=0
sumainpar=0
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)

for i in range(tam):
    #print(posicion",i,"elemento",vector[i])
    if vector[i]%2==0:
        print(vector[i],"es par")
        sumapar+=vector[i]
        print("La suma es",sumapar)
    else:
        print(vector[i],"es inpar")







