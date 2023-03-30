import datetime as d
 
def dia ():
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    dia=int(input('Ingree el dia: '))
    mes=int(input('Ingrese el mes:'))
    año=int(input('Ingrese el año: '))
    formato=(d.date(año,mes,dia))
    dia=dias_semana[formato.weekday()]
    print(dia)

dia()