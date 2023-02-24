try: #es la secuencia que se quiere evaluar
    #print(1/1))
    raise SyntaxError #es el error que quiero generar
except SyntaxError as e: #seutiliza la excepcion para que se genere este error, ademas se utiliza as para cambiar el nombre de la excepcion
    print(e) #se imprime el cambio de nombre de la excepcion
    print('Cierra el parentesis') #se imprime la respuesta que queremos dar
    
try:
    #raise ZeroDivisionError
    print(1/0)
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:
    print(zde)
    #print('prueba error')