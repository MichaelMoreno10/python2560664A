# Aqui se cree un diccionario con las palabras y la traduccion a frances

word=input("Ingrese un instrumento")

def traduccion(word):
    
    dictionary = {"La guitare" :"la guitarra",

"Le piano" : "el piano",

"La contrebasse" : "el contrabajo",

"La batterie" : "la batería",

"Le saxophone" :"el saxofón",

"La trompette" : "la trompeta",

"Le trombone" : "el trombón",

"Le violon" : "el violín"
 }
    
#esta funsion sirve para buscar la palabra en el diccionario y su traduccion. tambien sirve para mostrar cuantas palabras tienen en español e ingles
#y por ultimo muestra que tipo de palabra es
  
    if word in dictionary:
        
        traducir= dictionary[word]
        
        palabra= len(word)
        palabrat = len(traducir)
        
        tipo = "Sustantivo"
        
        
        return ("la palabra",word,"traducida al español es",traducir,
        "la palabra", word,"cuenta con", palabra, "letras", 
        "la palabra", traducir,"cuenta con",palabrat, "letras",
        traducir,"es un", tipo)
    else:
        
        return "La palabra no se encuentra en el diccionario."