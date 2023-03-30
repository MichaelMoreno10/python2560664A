import csv   #Importamos el archivo "csv"
diccio=[     #Se crea un diccionario
    {'name':'Alice','age':18},        #Dentro de ese diciionaroi se encuntra otro diccionario con los datos 
    {'name':'Bob','age':19},        
    {'name':'John','age':17}
]
header=['name','age']     #Una variable con otro diccionario y sus datos

with open('archivos/people.csv','w') as csvfile:   #La ruta del archivo con su cambio de nombre 
    writer=csv.DictWriter(csvfile,fieldnames=header)   #Se crea una variable local que va a almacenar lo que va a ir en la primera columna
    writer.writeheader()           #Se utiliza la variable con un metodo para crear la cabecera del archivo
    writer.writerows(diccio)      #Se utiliza la variable con un metodo para escribir lo demas del diccionario