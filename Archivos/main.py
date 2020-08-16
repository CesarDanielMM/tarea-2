import json
import xml.dom.minidom
import csv


def cargar_datos (ruta):
    with open(ruta) as contenido:
       resultado = json.load(contenido)
       contenido.close()
    return resultado

def cargar_datos2 (ruta2):
    resultado2 = xml.dom.minidom.parse(ruta2);
    return resultado2



if __name__ == '__main__':
    ruta = 'ArchivoJSON.json'
    ruta2 = 'ArchivoXML.xml'


    dict = cargar_datos(ruta)
    print("Archivo JSON:")
    print("Tipo de estructura de dato: Diccionario")
    for dict in dict:
        print(dict.get('nombre'),dict.get('carnet'),dict.get('facultad'),dict.get('inscrito2020'),dict.get('creditos'))


    dict2 =  cargar_datos2(ruta2)
    print("Archivo XML:")
    print("Tipo de estructura de dato: DOM")


    for elements in [0,1,2,3]:
        d = dict2.getElementsByTagName("reg")[elements]
        d1 = dict2.getElementsByTagName("nombre")[elements]
        d2 = dict2.getElementsByTagName("usuario")[elements]
        d3 = dict2.getElementsByTagName("contraseña")[elements]
        d4 = dict2.getElementsByTagName("pais")[elements]

        print(d.firstChild.data,d1.firstChild.data,d2.firstChild.data,d3.firstChild.data,d4.firstChild.data)

    print("Archivo CSV:")
    print("Tipo de estructura de dato: Reader")
    with open('ArchivoCSV.csv') as contenido3:
        resultado3 = csv.reader(contenido3)
        for row in resultado3:
            print("{0}, {1}, {2}, {3}. {4}".format(row[0],row[1],row[2],row[3],row[4]))












