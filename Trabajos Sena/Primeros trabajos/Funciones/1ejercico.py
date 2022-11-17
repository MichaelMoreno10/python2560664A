def medio(numero1,numero2,numero3):
    if numero1<numero3 and numero1>numero2:
        return numero1
    elif numero1>numero3 and numero1<numero2:
        return numero1
    elif numero2<numero3 and numero2>numero1:
        return numero2
    elif numero2>numero3 and numero2<numero1:
        return numero2
    else:
        return numero3 

      
        
numero1=int(input("Ingrese el primer numero:"))
numero2=int(input("Ingrese el segundo numero"))
numero3=int(input("Ingrese el tercer numero"))

print("El valor de la mitad es",medio(numero1,numero2,numero3))








