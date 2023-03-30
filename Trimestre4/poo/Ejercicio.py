from re import I


class producto:
    cont=0
    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio
 #getter   
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio
  #setter  
    def set_nombre(self,nombre):
        self.__nombre=nombre

    def set_precio(self,precio):
        self.__precio=precio
    def calculariva(self):
        i=self.__precio*0.19
        iva=self.__precio+i
        return f"{self.__precio} tiene un iva de {i} total {iva}"

producto1=producto("teclado",32000)
producto2=producto("mouse",10000)
producto3=producto("parlante",20000)

print(producto1.get_nombre())
producto1.set_nombre("tv")
print(producto1.get_nombre())

print(producto1.get_precio())
producto1.set_precio(15000)
print(producto1.get_precio())

print(producto1.calculariva())
print(producto1)

