#- De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou""áéíóú":
			contador += 1
	return contador

def es_vocal(letra):
    return letra in "aeiou"

      

cadena = "Hola mundo"
cadena_minuscula = cadena.lower()
cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}'' hay {cantidad} vocales")
cantidad_consonantes = 0
for letra in cadena_minuscula:
    if letra.isalpha() and not es_vocal(letra):
        cantidad_consonantes += 1
print(f"En la cadena '{cadena}' hay {cantidad_consonantes} consonantes")


