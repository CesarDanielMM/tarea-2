import xml.dom.minidom

ruta2 = 'ArchivoXML.xml'

dict2 = xml.dom.minidom.parse(ruta2)
print("Archivo XML:")
print("Tipo de estructura de dato:")
print(type(dict2))

for elements in [0, 1, 2, 3]:
    d = dict2.getElementsByTagName("reg")[elements]
    d1 = dict2.getElementsByTagName("nombre")[elements]
    d2 = dict2.getElementsByTagName("usuario")[elements]
    d3 = dict2.getElementsByTagName("contraseña")[elements]
    d4 = dict2.getElementsByTagName("pais")[elements]

    print(d.firstChild.data, d1.firstChild.data, d2.firstChild.data, d3.firstChild.data, d4.firstChild.data)