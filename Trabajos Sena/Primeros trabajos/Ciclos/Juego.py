numero=10#Numero que se desea adivinar 
control=0#Variable del ciclo
intentos=1#controla los intentos
print("Adivina el numero")
while (control==0):
    print("intento numero",intentos)
    print("Ingrese un numero")
    num= int(input())#solicitamos un numero para comparar
    if (num==numero):
        print("Adivinaste el numero")
        print("Utilizaste",intentos,"intentos")
        control=1
    elif(num>numero):
        print("El numero es menor")
        intentos+=1
    elif(num<numero):
        print("El numero es mayor")
        intentos+=1


