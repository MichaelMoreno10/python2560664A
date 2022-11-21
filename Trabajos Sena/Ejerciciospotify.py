play = {}
playlist = {
    "me porto bonito": {
        "autor":"bad bunny ft chencho C",
        "albun":"Un verano sin ti",
        "genero": "Urbano",
        "duracion": 3.11, 
        "lanzamiento":2022},
    "Es un secreto": {
        "autor":"Plan B",
        "genero":"Urbano",
        "albun":"House of pleasure",
        "duracion": 3.35,
        "lanzamiento":2010},
    "Ojitos chiquititos": {
        "autor":"Don Omar",
        "albun":"King of King",
        "genero": "Urbano",
        "duracion": 3.50,
        "lanzamiento":2008},
    "Sun da da": {
        "autor":"zion",
        "albun":"The perfect melody",
        "genero": "Urbano",
        "duracion": 5.30,
        "lanzamiento":2007},
    "5 letras":{
        "autor":"Alexis y fido",
        "albun":"sobre natural",
        "genero": "Urbano",
        "duracion": 3.16,
        "lanzamiento":2008} 
    }

cancion = input("ingrese el nombre de la cancion")
autor = input("ingrese el nombre del autor")
albun = input("ingrese el nombre del albun")
genero = input("ingrese el genero de la cancion")
duracion = float(input("ingrese la duracion de la cancion"))
lanzamiento = int(input("ingrese el año de estreno"))

def Nmusic ():
    play.update(cancion,autor,albun,genero,duracion,lanzamiento)
    return(play)

print(play)