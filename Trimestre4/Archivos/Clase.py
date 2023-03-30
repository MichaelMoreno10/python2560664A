class Persona:
    def __init__(self,Index,Year,Age,Name,Movie):
        self.__Index=Index
        self.__Year=Year
        self.__Age=Age
        self.__Name=Name
        self.__Movie=Movie

    def nombrecompleto(self):
        return self.__Name+" "+self.__Age 

    def todo(self):
        self.__Name+"  "+self.__Name   


class Persona2:
    def __init__(self,Index2,Year2,Age2,Name2,Movie2):
        self.__Index2=Index2
        self.__Year2=Year2
        self.__Age2=Age2
        self.__Name2=Name2
        self.__Movie2=Movie2

    def pelicula(self):
        return self.__Movie+" "+self.__Movie2

         