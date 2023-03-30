class Curso:  #Se crea la clase "Curso"
    def __init__(self,titulo): #Se crea el constructor con un parametro en la funcion
        self.__titulo=titulo #se asigna el parametro a la clase curso

    def getTitulo(self): #Se crea una funcion para visualizar 
        return self.__titulo  #Retorna el atributo nombre de la clase 

class Aprendiz:    #Se crea la clase "aprendiz"
    def __init__(self,nombre):  #Se crea el constructor con un parametro
        self.__nombre=nombre #se asigna el parametro a la clase curso
        self.__cursos=[]  #Se asigna una lista vacia para "cursos"

    def agregarCurso(self,nombreCursito):  #Se crea una funcion par agregarcurso
        cursito=Curso(nombreCursito)    #se asigna el parametro a la clase curso
        self.__cursos.append(cursito)  #se asigna el parametro a la clase curso

    def getCursos(self):      #Se crea una funcion para visualizar
        return self.__cursos  #Se retorna el atributo nombre de la clase
    
ap=Aprendiz('Sofia')  #Se llam el metodo
ap.agregarCurso('Python Basico')  #Se utiliza el metodo
ap.agregarCurso('Python Intermedio') #Se utiliza el metodo

for c in ap.getCursos():   #Se crea un for para recorre "getCursos"
    print(c.getTitulo())  #Se imprime la funcion "getTitulo"

del ap    #Se elimina la variable "ap"