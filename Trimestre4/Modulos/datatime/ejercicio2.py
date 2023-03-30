import datetime as d


def edad(fecha_nacimiento, fecha_actual):
    if fecha_nacimiento < fecha_actual:
        edad=fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        print(f'Esa persona, objeto o animal tiene {edad} años')
    else:
        print('No ha nacido')

fecha_nac = d.date(2004,12,14)
fecha_act=d.date.today()
edad(fecha_nac,fecha_act)