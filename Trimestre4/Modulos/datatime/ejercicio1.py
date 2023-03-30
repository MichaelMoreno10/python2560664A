import datetime as d

def navidad():
    dia_presente= d.date.today()
    dia_navidad=d.date(dia_presente.year,12,25)
    if dia_presente>dia_navidad:
        dia_navidad=d.date(dia_presente.year+1,12,25)
        dia_faltante=(dia_navidad-dia_presente).days
        return(f'Faltan {dia_faltante} para navidad')    
    else:
        dia_faltante=(dia_navidad-dia_presente).days
        return(f'Faltan {dia_faltante} para navidad')
         
print(navidad())
