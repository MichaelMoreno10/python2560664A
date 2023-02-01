def tablamultiplicar(x):
    n=5
    i=1
    while i <11:
        print(n,"multiplicado por ",i,"es igual a",n*i)
        i +=1
    
    


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


def superarnumero(numero):
    n = 0
    suma = 0
    while (suma < numero):
        n = n + 1
        suma = 0
        for i in range(n +1):
            suma = suma + 1
    return 'El número natural minimo para superar el número ingresado es',n        


def numerosIguales(a,b,c):
    if a == b & b == c:
        return 'Los tres números son iguales'
    elif a == b or b == c or c == a:
        return 'Hay dos números iguales'
    else:
        return 'Todos los números son diferentes'

def invertirNumero(n):
    r = 0
    while n != 0:
        c = n % 10
        r = r * 10 + c
        n = n // 10

    return r

