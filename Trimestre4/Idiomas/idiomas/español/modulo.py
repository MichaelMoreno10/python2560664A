# Aqui se cree un diccionario con las palabras y la traduccion a ingles


x=input("Ingrese un instrumento")

def translate_word(x):
    
    dictionary = {"Acordeon" : "Accordion",
 "gaita" : "Bagpipes",
 "batería" : "Drums",
 "chelo" : "Cello",
 "contrabajo" : "Double bass",
" flauta" : "Flute",
 "flauta dulce" :"Recorder",
 "piano" : "piano",
 " Grand piano" : "Grand piano",
 "guitarra" : "Guitar",
 "pandereta"  : "Tambourine",
 "trompeta"  :"Trumpet",
 "trombón"  : "Trombone",
 "saxofón"  : "Saxophone",
 "guitarra acústica" :"Acoustic guitar",
 "guitarra eléctrica" : "Electric guitar",
 "bajo" :"Bass guitar or bass",
 "maracas" :" maracas",
 "Guitarra" : "Guitar",
 "órgano" :"Organ",
 "armónica" :"Harmonica",
 "fagot" :"Bassoon" ,
 "Bongo:": "bongo",
 "clarinete" :" Clarinet",
 "platillos": "Cymbals ",
 "castañuelas": " Castanets",
 "violoncelo" : "Cello"
 }
    
#esta funsion sirve para buscar la palabra en el diccionario y su traduccion. tambien sirve para mostrar cuantas palabras tienen en español e ingles
#y por ultimo muestra que tipo de palabra es

    if x in dictionary:
        
        traducir= dictionary[x]
        
        palabra= len(x)
        palabrat = len(traducir)
        
        tipo = "Sustantivo"
        
        
        return ("la palabra",x,"traducida al idioma ingles es",traducir,
        "la palabra", x,"cuenta con", palabra, "letras", 
        "la palabra", traducir,"cuenta con",palabrat, "letras",
        x,"es un", tipo)
    else:
        
        return "La palabra no se encuentra en el diccionario."#si se escribe una palabra que no este en el diccionario manda este mensaje
     

 