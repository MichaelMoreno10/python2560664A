class material():
    def __init__(self,titulo,tipo,autor):
        self.__tituloMaterial = titulo
        self.tipoMaterial = tipo
        self.autorMaterial = autor


    def getTitulo(self):
         return self.__tituloMaterial
    
    def setTitulo(self,titulo):
        self.__tituloMaterial=titulo

    def getTipo(self):
        return self.tipoMaterial
    
    def setTipo(self,tipo):
        self.tipoMaterial=tipo

    def getAutor(self): 
        return self.autorMaterial
    
    def setAutor(self,autor):
        self.autorMaterial= autor



class libro(material):
    def __init__(self, titulo, tip  o, autor, editorial):
        material.__init__(self,titulo,tipo,autor)
        self.editorial = editorial
    def getEditorial(self):
        return self.editorial
    
    def setEditorial(self,editorial):
        self.editorial = editorial


    
class revista(material):
    def __init__(self, titulo, tipo, autor,edicion):
        material.__init__(self,titulo, tipo, autor)
        self.__edicion=edicion

    def getEdicion (self):
        return self.edicion

    def setEdicion(self,edicion):
        self.edicion = edicion 


i=libro("El dinero","economia","edgar jacinto","la calle")
print("nombre del libro",i.getTitulo())
i.setTitulo("El tiempo")
print("Una segunda opcion",i.getTitulo())
print("Su tipo es:",i.getTipo())
print("El autor es:",i.getAutor())



o=revista("Descarte","animada","Andres","la especial")
print("Seccion de revistas")
print("Titulo del libro",o.getTitulo())
o.setTitulo("Ahorro")
print("Otro puede ser",o.getTitulo())
print("Su tipo es:",i.getTipo())
print("El autor es:",i.getAutor())






        



class lector :
    def __init__(self,nombre,direccion,telefono):
        self.__libro=[]
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        
    def getnombre(self,):
        return self.__nombre

    def setnombre (self,nombre):
        self.__nombre =nombre

    def getdireccion (self,):
        return self.__direccion

    def setdireccion (self,direccion):
        self.__direccion=direccion

    def gettelefono(self,):
        return self.__telefono

    def settelefono(self,telefono):
        self.__telefono=telefono

    def reserva(self,material):
        self.__libro.append (material)    


class estudiante (lector):
    __codigoestudiante=12
    def __init__ (self,nombre,direccion,telefono):
        lector .__init__(self,nombre,direccion,telefono)
        estudiante.__codigoestudiante

    def getcodigoestudiante (self):
        return estudiante.__codigoestudiante

    def setcodigoestudiante (self,codigoestudiante):
        self.__codigoestudiante =codigoestudiante
    
l=estudiante("Julio","3 sur","321426356")
print("codigo de estudiante",l.getcodigoestudiante())

class docente(lector):
    __codigodocente=32
    def __init__(self,nombre,direccion,telefono):
        lector.__init__(self,nombre,direccion,telefono)
        docente.__codigodocente

    def getcodigoDoc (self):
        return docente.__codigodocente
    def setcodigoDoc (self,codigo):
        self.__codigodocente=codigo

p=docente("Ricardo","4s","3167372938")
print("codigo de profesor",p.getcodigoDoc())

class bibliotecario():
    id__idbibliotecario=54
    def __init__(self,nombre):
        self.__nombre=nombre
    def getidbibliotecario (self):
        return self.id__idbibliotecario
    
    
v=bibliotecario("fernando")
print("Codigo Bibliotecario",v.getidbibliotecario())



class pedidio():
    def __init__(self,usuario,material,):
        self.pedido={}
        self.__usuario=usuario
        self.__material=material

    def getusuario(self):
        return self.__usuario

    def getmaterial(self):
        return self.__material    

    def getTodo(self):
        print(self.getusuario())
        print(self.getmaterial())
        
d=pedidio("Carlos","libro")
print(d.getusuario())
print(d.getmaterial())
l.reserva(i)
l.reserva(o)



          





