def try_syntax(numerator, denominator): #se crea una funcion en la cual hay dos parametros
    try: #Se crea el try para la secuencia que se quiere evaluar
        result = numerator / denominator  #Se hace la operacion con los valores que tengamos como parametro de la funcion
        print(f"In the try block: {numerator}/{denominator}",result) #se imprime la cadena que esta entre comillas y tambien la division que se va a ejecutar dependiendo de los datos que tengamos de parametro
        #quiero ver el resultado de la operacion en el print  RPTA: Se hace la operacion antes del print y se llama la variable en el print
        result = numerator / denominator #Se hace la operacion con los valores que tengamos como parametro de la funcion
    except ZeroDivisionError as zde: #Se coloca la excepcion "ZeroDivisionError" por si un parametro llega hacer cero, ademas se cambia el nombre de la funcion por "zde"
        print(zde) #se imprime la variable con nombre "zde"
    else: #ssse coloca un else por si no es necesario utilizar la excepcion y asi pueda imprimir lo de la siguiente linea
        print('The result is:', result) #se imprime una cadena de letras y la variable "result"
        return result #el retorno de la funcion con la variable que ejecuta la operacion de la funcion
    finally: #se utiliza como una sentencia de finalizacion del programa
        print('Exiting') #se imprime una cadena de texto
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 5)) #se imprime la funcion con su respectivo resultado, ademas le damos los parametros para realizar la funcion