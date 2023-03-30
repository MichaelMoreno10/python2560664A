values = (1, 5) #se crea una tupla
#x,y=10,12
#print(divmod(10,3))
try: #Se crea el try para la secuencia que se quiere evaluar
    q, r = divmod(*values) #las variables toman el valor de la tupla, el * hace que cada variable se le asigne un valor y no la tupla en general, ademas se hace una division con el divmod
    #print('valor de q=',q)
    print(f'q={q}') #se imprime la variable con su respectivo  resultado
    print(f'r={r}') #se imprime la variable con su respectivo  resultado
except (ZeroDivisionError, TypeError) as e: #esta la excepcion por si llagan a dividir por 0 o ingresan un tipo de dato que no es, ademas se le cambia el nombre a la expcion por "e"
    print(type(e), e) #se imprime la variable "e", y se coloca el "type" para saber el tipo de dato que es 