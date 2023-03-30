
def suumar (a,b):
    try:
        c= a+b
        print("Usted va a realizar una suma")
    except TypeError:
        print("Ingreso un valor no deseado")
    else:
        print(c)    
suumar ("e",4)    