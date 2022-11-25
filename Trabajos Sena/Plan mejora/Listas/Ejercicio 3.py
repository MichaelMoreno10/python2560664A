# Contar las apariciones de cada número en una lista 
 
Lista=[ 0, 5, 8, 0, 5, 4, 4, 0, 0, 5, 0 ] 
 
reconteo=[0] *10 
 
for i in Lista : 
 reconteo[i] += 1 
 
for i in range(10) : 
 if reconteo[i] > 0 : 
   print("La cifra ",i," aparece", reconteo[i]," vez") 
 
