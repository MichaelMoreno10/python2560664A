palabra = "esdrújula"

if len(palabra) <= 2:
    print("La palabra es aguda")
elif palabra[-1] in "nNsS":
    print("La palabra es aguda")
elif palabra[-2:] in ["as", "es", "os"]:
    print("La palabra es grave")
elif palabra[-3] in "aeiouáéíóú":
    print("La palabra es esdrújula")
else:
    print("La palabra es sobresdrújula")
