def ErrordeLlave():
    try:
        animal=input("Ingrese el tipo de  animal: ")
        diccionario={'Mamifero':['Perro', 'Gato','León'],'Aves':['Loro','Perico','Paloma']}
        print(diccionario[animal])
    except KeyError:
        print("KeyError: Llave no encontrada ")

ErrordeLlave()