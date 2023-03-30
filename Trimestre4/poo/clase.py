class Ejemplo ():
    def __init__(self,var):
        self.__var=var
        print('Metodo Constructor')
    def set_ejemplo (self,var):
        self.__var=var
    def get_ejemplo (self):
        return self.__var
    
objet=Ejemplo('hola')
print(objet.get_ejemplo())
objet.set_ejemplo('chao')
print(objet.get_ejemplo())



class Ejemplo2 ():
    __lista=[]
    def __init__(self,tele):
        self.__telefono=tele
        Ejemplo2.__lista.append(self.__telefono)
    def set_telefono (self,tele):
        self.__telefono=tele
    def get_telefono (self):
        return self.__telefono
    def get_lista ():
        return Ejemplo2.__lista
    
objet2=Ejemplo2(321456887)
objeto3=Ejemplo2(32148448)


objeto3.tele2=321554488


print(objet2.get_telefono())
objet2.set_telefono(12345)
print(objet2.get_telefono())


print(Ejemplo2.get_lista())


print(objeto3.tele2)

print(objeto3.tele2)



print(objeto3.__dict__)
print(objet2.__dict__)


class ExampleClass:
    attri = 1
    def __init__(self):
        self.attr = 1

m=ExampleClass()
print(hasattr(m, 'attr'))
print(hasattr(ExampleClass,'attri'))
print(hasattr(ExampleClass, 'prop'))