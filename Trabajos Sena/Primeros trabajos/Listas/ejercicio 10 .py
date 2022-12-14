import random
def parimpar(num):
    if num%2==0:
        print("par")
    else:
        print("impar")

lista=[]
for i in range(10):
     lista.append(round(random.randrange(100)))            
print(lista)
for i in lista:
    print(i)
    parimpar(i)



def sumadivisores(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum
def amigos(x,y):
    sumx=sumadivisores(x)
    sumy=sumadivisores(y)
    if sumx==y and sumy==x:
        return"son amigos"
    else:
        return"no son amigos"

print(amigos(220,284))            


import random
def sumlista(lista):
    sum==0
for i in range 




def llenarlista(lista):
    tam=round(random.randit(5,15))
    for i in range(tam):
        lista.append(round(random.randrange(100)))
    return lista

list=[]
list=llenarlista(list)
int(list)
print(sumlista(list))





