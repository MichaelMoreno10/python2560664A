import random 

rango=random.randint (10,25)
vector=[round(random.random()*100)for n in range(rango)]
print("lista:", vector) 
for i in vector:
    n=1
    cont=0
    while(n>=n):
        if i%n==0:
            cont+=1
        i+=1
    if not cont>2 or n <=1:
        print("el numero",n,"es primo") 
                  