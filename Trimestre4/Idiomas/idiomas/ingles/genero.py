
#Diccionario de ingles a español

word=input("Ingrese un instrumento")

def translate_word(word):
    
    dictionary = {"Accordion" : "acordeón",
 "Bagpipes" : "gaita",
 "Drums" : "batería",
 "Cello" : "chelo",
 "Double bass" : "contrabajo",
" Flute" : "flauta",
 "Recorder" :"flauta dulce",
 "Piano" : "piano",
 "Grand piano " : "Piano de cola",
 "Guitar" : "guitarra",
 "Tambourine"  : "pandereta",
 "Trumpet"  :"trompeta",
 "Trombone"  : "trombón",
 "Saxophone"  : "saxofón",
 "Acoustic guitar" :"guitarra acústica",
 "Electric guitar" : "guitarra eléctrica",
 "Bass guitar or bass" :"bajo",
 "Maracas" :" maracas",
 "Guitar" : "Guitarra",
 "Organ" :"órgano",
 "Harmonica" :"armónica",
 "Bassoon" :"fagot" ,
 "Bongo:": "bongo",
 "Keyboard" : "teclado",
 "Clarinet" :" clarinete",
 "Cymbals": "platillos ",
 "Castanets": " castañuelas",
 "Cello" : "violoncelo"
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
     
#print(translate_word(word)) 
 