#ejerciocio 6 de ciclos
n=0
def numeros_opuestos(n):
    contador=0
    while(n>=0):
        n=int(input("introduzca numeros"))
        if n>=0:
            contador+=1
        else:
            print("esta fue la cantidad de numeros positivos registrados",contador)

            numeros_opuestos(n)
