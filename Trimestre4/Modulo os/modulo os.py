"""El módulo llamado os permite interactuar con tu sistema operativo usando Python
El módulo os te permite:

Obtener información sobre el sistema operativo.
Manejar procesos.
Operar en streams de E/S usando descriptores de archivos.

El módulo os te permite distinguir rápidamente el sistema operativo mediante el atributo name
posix: obtendrás este nombre si usas Unix.
nt: obtendrás este nombre si usas Windows.
java: obtendrás este nombre si tu código está escrito en Jython. """

import os
#print(os.name)

#El módulo os proporciona una función llamada mkdir, la cual,te permite crear un directorio
#La función listdir devuelve una lista que contiene los nombres de los archivos y directorios que se encuentran en la ruta pasada como argumento.


#os.mkdir("my_first_directory")
#print(os.listdir())

#La función makedirs permite la creación recursiva de directorios, lo que significa que se crearán todos los directorios de la ruta.

#os.makedirs("my_first_directory/my_second_directory")
#os.chdir("my_first_directory")
#print(os.listdir())
#Para moverte entre directorios, puedes usar una función llamada chdir, que cambia el directorio de trabajo actual a la ruta especificada.


#getcwd devuelve informacion sobre el directorio de trabajo actual

#os.chdir("my_first_directory")
#print(os.getcwd())
#os.chdir("my_second_directory")
#print(os.getcwd())

#rmdir= funcion para eliminar un SOLO directorio
#removedirs= funcion para eliminar directorios y subdirectorios


#os.rmdir("my_first_directory")
#print(os.listdir())

#os.removedirs("my_first_directory/my_second_directory")
#print(os.listdir())


#Otra forma para crear un directorio
#returned_value = os.system("mkdir my_first_directory")
#print(returned_value)

#comprobacion si una carpeta existe o no

#if os.path.exists("carpeta1")==True:
#       print("la carpeta ya existe")

#else:
#    os.mkdir("carpeta1")
#    print("La carpeta fue creada con exito")    