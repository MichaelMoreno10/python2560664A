""""class Persona: #Se define la clase la cual se llama "persona"
    def __init__(self,nombre): #se crea una funcion con sus parametros ademas tambien se encuentra el constructor
        self.__nombre=nombre #se asigna el parametro a la clase persona
        #print('Constructor Activado')        

    def getNombre(self): #se crea una funcion  para visualizar 
        return self.__nombre #Retorna el atributo nombre de la clase

    def setNombre(self,nombre): #Se cre una funcion con sus parametros 
        self.__nombre=nombre # se asigna el arametro a la clase persona 


ob=Persona('Maria') 
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob)) """""

class Persona:                  #se define la clase
    def __init__(self,nombre):  #funcion con parametros incluyendo el contructor
        self.__nombre=nombre    
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

ob=Persona('Michael')
print(ob.getNombre())
ob.setNombre('Julian')
print(ob.getNombre())
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,ficha):
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('Michael',2560664)
print(app.getFicha())
print(app.getNombre())

class Documento(Persona):
    def __init__(self, nombre,documento):
        Persona.__init__(self,nombre)
        self.__documento=documento

    def getDocumento(self):
        return self.__documento

    def setDocumento (self,documento):
        self.__documento=documento

asd=Documento("Michael",107123546)  
print(asd.getDocumento())      
asd.setDocumento("23456327")   
print("segundo documento",asd.getDocumento())


        

