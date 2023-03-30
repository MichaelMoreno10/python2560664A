from aprendiz import *      #Se crea una importacion de la clase aprendiz 
from curso import *         #Se crea una importacion de la clase aprendiz

nombre=input('ingrese nombre del aprendiz')  #Se crea una variable que va almacenar un dato ingresado por teclado
documento=int(input('ingrese documento del aprendiz'))  #Se crea una variable donde se va almacenar un dato entero ingresado por teclado
ficha=input('ingrese ficha del aprendiz')    #Se crea una variable que va almacenar un dato ingresado por teclado

ap=Aprendiz(ficha,nombre,documento)  #Se crea una variable que va a almacenar lo que contiene la clase "aprendiz"

nombreCurso=input('ingrese nombre del curso') #Se crea una variable que va almacenar un dato ingresado por teclado
horas=int(input('ingrese intensidad horaria del curso'))  # se crrea una variable que va almacenar un dato tipo entero ingresado por teclado
c1=Curso(nombreCurso,horas)   #Se crea una variable donde se llama la clase curso con sus respectivos parametros
ap.agregarCurso(c1)   #Se llama el metodo agregarcurso con la variable "c1"

with open('Archivos/aprendices.txt','a') as flujo:    #Se utiliza un metodo para decirle donde esta nuestro archivo con la variable local donde se guarda todo lo del archivo
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')  #Se llama los metodos get 