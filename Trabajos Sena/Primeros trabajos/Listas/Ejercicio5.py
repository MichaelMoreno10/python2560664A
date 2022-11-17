from cmath import sqrt 
import random
import statistics
tam= random.randint(10,25)
sum=0
v=[]
for i in range(tam):
    v.append(round(random.random()*100))
    v.sort()
for i in range(tam):
    sum+=v[i]
    media=sum//v.__len__()
print(v)
print("la mediana es:",statistics.median(v))
media=float(media) 
