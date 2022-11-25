#programa que termina al ingresar 0
suma=0
Num=int(input("Ingrese un número, ingresa 0 para terminar: "))
while Num>0:
        if Num!=0:
            suma+=Num
        Num=int(input("Ingrese un número, ingresa 0 para terminar:"))
print(suma)