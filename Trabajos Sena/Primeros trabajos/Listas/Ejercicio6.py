import random
rang = int(input("Cuantos numero desea que se muestren "))
fib=[0,1]
for i in range(rang-2):
    fib.append(fib[-1]+fib[-2])
print(fib)    

