def ErrorV():
    try:
        i=int(input('Ingrese un numero'))
        if i>=0:
            print('El numero es positivo ')
        else:
            i<=0
            print('El numero es negativo')
    except ValueError:
        print('A ingresado un dato erroneo')


ErrorV()