import csv
with open ("archivos/oscar_age_female.csv","r") as oscarmujer:

    csvReader=csv.reader(oscarmujer)
    for i in csvReader:
        print("Index:"[0])
        print("Year:"[1])
        print("Age:"[2])
        print("Name:"[3])
        print("Movie:"[4])


