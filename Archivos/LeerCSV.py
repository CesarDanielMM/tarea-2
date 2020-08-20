import csv

print("Archivo CSV:")
print("Tipo de estructura de dato:")
with open('ArchivoCSV.csv') as contenido3:
    resultado3 = csv.reader(contenido3)
    print(type(resultado3))
    for row in resultado3:
        print("{0}, {1}, {2}, {3}. {4}".format(row[0], row[1], row[2], row[3], row[4]))

