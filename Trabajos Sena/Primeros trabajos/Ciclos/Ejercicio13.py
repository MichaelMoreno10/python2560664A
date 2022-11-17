Num=int(input("Ingrese número de 9 cifras: "))
N9=Num%10
N8=int((Num%100)/10)
N7=int((Num%1000)/100)
N6=int((Num%10000)/1000)
N5=int((Num%100000)/10000)
N4=int((Num%1000000)/100000)
N3=int((Num%10000000)/1000000)
N2=int((Num%100000000)/10000000)
N1=int((Num-(Num%100000000))/100000000)

print(str(N9)+str(N8)+str(N7)+str(N6)+str(N5)+str(N4)+str(N3)+str(N2)+str(N1))