class Vehiculo:                                         #Definmos una clase la cual llamaremos "vehiculo"
    def __init__(self,tipo):                            #creamos una funcion donde se encuentra el constructor y tenemos un parametro
        self.tipo=tipo                                  #crea una variable de instancia que guarda el argumento
    def descripcion(self):                              #una funcion 
        print('Soy generico no tengo descripcion',self.tipo) #Imprime una cadena de texto, con el tipo
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):                                  #crea una funcion para el visualizar el tipo
        return self.tipo                                #retorna el tipo
        #return Vehiculo.tipo
    def __str__(self):                                  #   se crea un metodo
        return 'Soy objeto de la clase Vehiculo'        # retorna una cadena

class Herramienta:                                      #se crea otra clase lllamada "herramienta"
    def __init__(self,proposito):                       #se crea el constructor y una funcion con sus parametros
        self.__proposito=proposito                      #crea una variable de instancia que guarda el argumento
    def getProposito(self):                             #
        return self.__proposito
    def __str__(self):
        return 'Soy objeto de la clase Herramienta'
class Terrestre(Vehiculo,Herramienta):
    def __init__(self,tipo,proposito):
        Herramienta.__init__(self,proposito)
        Vehiculo.__init__(self,tipo)        
    def datos(self):
        print('Tipo: ',super().getTipo())
        print('Tipo: ',super().getProposito())
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())

