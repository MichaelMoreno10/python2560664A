class libro:
    def __init__(self,titulo,tipo,autor,editorial):
        self.__titulo=titulo
        self.tipo=tipo
        self.autor=autor
        self.editorial=editorial
    def agregartitulo(self):
        return titulo



class lector :
    def __init__(self,nombre,direccion,telefono):
        self.nombre=input("Ingrese su nombre ")
        self.direccion=input("Ingrese su direccion")
        self.telefono=input("Ingrese su telefono")

    def hacerpedido(self,titulo,codigo):


