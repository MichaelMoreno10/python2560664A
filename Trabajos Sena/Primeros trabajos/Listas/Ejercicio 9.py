import random 
vector=[]
rango=random.randint(10,25)
for i in range(rango):
    vector.append(round(random.random()*100))
print("La lista sin ordenar es;", vector)
vector.sort()
print("La lista ordenada es:", vector)
mitad=int(rango//2)
if rango%2==0:
    mediana=(vector[mitad-1]+vector[mitad])//2
else:
    mediana=vector[mitad]
print("la longitud del vectores", rango)
print("la mediana del vector es", mediana)        