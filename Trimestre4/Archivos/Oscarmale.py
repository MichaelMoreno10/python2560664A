import csv
with open ("archivos/oscar_age_male.csv","r") as oscarhombre:

    csvReader=csv.reader(oscarhombre)
    for i in csvReader:
        print("Index2:"[0])
        print("Year2:"[1])
        print("Age2:"[2])
        print("Name2:"[3])
        print("Movie2:"[4])