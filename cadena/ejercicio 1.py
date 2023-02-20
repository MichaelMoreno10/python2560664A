## Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez

print("Ejercio")
print("Caracteres repetidos")

cadena = str(input("Digite la cadena: "))
contador = 0

for letra in cadena:
    for i in letra:
        if letra == (letra):
            contador += 1
print (contador)