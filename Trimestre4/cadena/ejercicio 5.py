
s=input("Ingrese una frase")
def suma(c):
    total=0
    for i in c:
        total+=ord(i)
    return total

print("El total es:", suma(s))