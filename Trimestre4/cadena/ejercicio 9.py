#- Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última
cadena = "abcdefghij"

for i in range(2, len(cadena) + 1):
    subcadena = cadena[:i]
    print(subcadena)