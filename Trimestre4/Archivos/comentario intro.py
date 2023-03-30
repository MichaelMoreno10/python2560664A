flujo=open('archivos/inicio.txt','a')     #Es una variable con un metodo para decirle que tome la ruta donde se encuentra el archivo
datos=flujo.read()     #una nueva variable "datos" con un metodo que es para que lea lo almacenado en la variable "flujo"
print(datos)   #Se llama la segunda variable "datos"
flujo.write('\nCuando estudian con juicio')  #la variable"flujo" se le asigna un metodo el cual sirve para escribir cualquier cosa en un archivo de extencion txt
datos=flujo.read()  
print(datos)

#La ruta absoluta es la que se toma desde el disco principal y la ruta relativa es do
