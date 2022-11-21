horasextras= {}

while True:
    name = input("Ingresa el nombre del trabajador: ")
    if name == '':
        break
    
    score = int(input("Ingresa las horas extras trabajadas en el dia (0-20): "))
    if score not in range(0, 21):
	    break
    
    if name in horasextras:
         horasextras[name] += (score,)
    else:
         horasextras[name] = (score,)
        
for name in sorted (horasextras.keys()):
    adding =0
    counter =0
    for score in  horasextras[name]:
        
        adding += score * 5208
        counter += 1
        print(name, "Hizo",counter, "Horas extras")  
        print(name, ":", adding )
    
   