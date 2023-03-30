def año ():
    try:
        a=int(input("Introduzca un año"))
        if a > 2023:
            print("Estas en el futuro")
        else:
            a < 2023
            print("Estas en el pasado") 
    except ValueError:
        print("No has ingresado un año") 
        año()       
año()            