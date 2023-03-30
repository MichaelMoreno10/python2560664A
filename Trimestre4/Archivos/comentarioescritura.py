import csv    #Se importa el archivo "csv"
header=['Fruit','Price']    #Se crea una variable que va a contener un diccionario
rows=[['Apple',1200],       #Se crea otra variable con un diccionario
      ['Berry',2000],
      ['Lemon',1000],
      ['Melon',3000],
      ['Grapes',4000],
      ['Pear',2000]]

with open ('archivos/example.csv','w') as csvfile:    #La ruta del archivo con su cambio de nombre
    csvwriter=csv.writer(csvfile)     #se cfea una variable que va hacer igual al archivo que importamos con un metodo para escribir en el archivo de xsv
    csvwriter.writerow(header)    #Se utiliza la variable con un metodo para escribir la primera fila
    csvwriter.writerows(rows)   #Se utiliza la variable con un metodo para escribir lo demas 