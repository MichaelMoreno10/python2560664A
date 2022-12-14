import random

contador = 0
suma = 0
prome = 0
moda = 0
media = 0
desEstandar = 0

vec = []
vec2 = [] 

rango = random.randint(10,25)

for i in range(rango):
    vec.append(round(random.random()*100))
    vec2 = vec
    contador += 1
    suma += vec[i]
    prome = suma / contador

print("Los numeros aleatorios son", rango,"y son los siguientes",vec)
print('La suma de los números generados es',suma)
print('El promedio de los números generados es',prome)
