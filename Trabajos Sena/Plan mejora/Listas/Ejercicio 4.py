# Encontrar todos los números primos entre 0 y 100 
print("Números primos encontrados: ")
for i in range(1,100) : 
   primo = True 
   for v in range(2,i) : 
       if i%v == 0 : 
           primo = False 
   if primo : 
        print(i,end=" ") 

         