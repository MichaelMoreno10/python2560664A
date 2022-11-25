#Hacer el algoritmo de Euclides para calcular el máximo común divisor de dos números enteros

a=int(input("Ingrese un número: "))
b=int(input("Ingrese el segundo número: "))
if a<b:
    while b>0:
        r=a%b
        a=b
        b=r
    print(a)
else:
    print("No se puede hallar el mcd")