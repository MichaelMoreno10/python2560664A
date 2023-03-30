class Producto ():
    __cont=0
    suma=0
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        Producto.__cont+=1
        
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre=nombre
    
    
    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio
    
     
    def calcular_iva (self):
        i=self.__precio*0.19
        iva=self.__precio+i
    
        
        return f'Valor sin iva {self.__precio} tiene un iva de {i} total {iva}'
    
    def contador():
        return f'Se han creado {Producto.__cont} productos'
    


produc1=Producto('usb',3500)
produc2=Producto('Nevera',100)
produc3=Producto('computer',500)
produc4=Producto('teclado',500)

     
print(produc1.get_nombre())
produc1.set_nombre('TV')
print(produc1.get_nombre())


print(produc1.get_precio())
produc1.set_precio(2000)
print(produc1.get_precio())


print(produc1.calcular_iva())
print(produc2.calcular_iva()) 


print(Producto.contador())