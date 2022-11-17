n1 = int(input('Ingrese el primer numero'))
n2 = int(input('Ingrese el segundo numero'))
n3 = int(input('Ingrese el tercer numero'))

if n2 > n1:
    if n1 > n3:
        print('El numero del medio es',n1)
if n3 > n1:
    if n1 > n2:
        print('El numero del medio es',n1)
if n1 > n2:
    if n2 > n3:
        print('El numero del medio es',n2)
if n3 > n2:
    if n2 > n1:
        print('El numero del medio es',n2)
if n1 > n3:
    if n3 > n2:
        print('El numero del medio es',n3)
if n2 > n3:
    if n3 > n1:
        print('El numero del medio es',n3)