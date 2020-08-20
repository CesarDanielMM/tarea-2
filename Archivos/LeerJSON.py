import json

ruta = 'ArchivoJSON.json'

with open(ruta) as contenido:
    dict = json.load(contenido)
    contenido.close()

    print("Archivo JSON:")
    print("Tipo de estructura de dato:")
    print(type(dict))
    for dict in dict:
        print(dict.get('nombre'), dict.get('carnet'), dict.get('facultad'), dict.get('inscrito2020'),
              dict.get('creditos'))