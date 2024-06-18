'''
load vs loads, dump vs dumps
'''

''' 
Convertir Diccionario a JSON (Serialización)
Para convertir un diccionario de Python a una cadena JSON, usa la función json.dumps()

Escribir JSON a un Archivo
Para escribir datos JSON a un archivo, usa json.dump()


Convertir JSON a Diccionario (Deserialización)
Para convertir una cadena JSON a un diccionario de Python, usa la función json.loads():

Leer JSON desde un Archivo
Para leer datos JSON desde un archivo, usa json.load()

'''


''' El módulo json contiene funciones tanto para leer y escribir desde y hacia cadenas Unicode, como para leer y 
escribir desde y hacia archivos. Estas funciones se diferencian por la letra s al final del nombre de la función
En estos ejemplos usamos un objeto StringIO, pero las mismas funciones se aplicarían para cualquier objeto similar a un 
archivo.

Aquí utilizamos las funciones basadas en cadenas:
'''

import json
data = {u"foo": u"bar", u"baz": []}     # en python3 todas las cadenas ya son unicode!
json_string = json.dumps(data)
print(json_string)
# {"foo": "bar", "baz": []}
print(json.loads(json_string))
# {"foo": "bar", "baz": []}

''' Y aquí utilizamos las funciones basadas en archivos.'''

import json
from io import StringIO

# Creamos un archivo en memoria
json_file = StringIO()

# Creamos datos en formato JSON
data = {u"foo": u"bar", u"baz": []}

json.dump(data, json_file)      # Volcamos (dump) los datos JSON en el archivo

json_file.seek(0)       # Movemos el cursor al inicio del archivo antes de leer

json_file_content = json_file.read()        # Leemos el contenido del archivo
print(json_file_content)        # {"foo": "bar", "baz": []}

json_file.seek(0)       # Movemos el cursor al inicio del archivo antes de leer

print(json.load(json_file))        # Cargamos (load) los datos JSON desde el archivo
# {'foo': 'bar', 'baz': []}

''' 
En lugar de capturar el valor de retorno. También es importante tener en cuenta que debes posicionarte al inicio 
del archivo antes de leer o escribir, para evitar la corrupción de datos. Al abrir un archivo, el cursor se coloca en 
la posición 0, por lo que lo siguiente también funcionaría.
'''
import json
json_file_path = './data.json'
data = {u"foo": u"bar", u"baz": []}
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file)
with open(json_file_path) as json_file:
    json_file_content = json_file.read()
    print(json_file_content)
# {'foo': 'bar', 'baz': []}
with open(json_file_path) as json_file:
    print(json.load(json_file))
# {'foo': 'bar', 'baz': []}

''' 
Tener ambas formas de manejar datos JSON te permite trabajar de manera idiomática y eficiente con formatos que se basan 
en JSON, como el JSON por línea de pyspark
'''

# cargando desde un archivo
data = [json.loads(line) for line in open(file_path).splitlines()]

# volcando a un archivo
with open(file_path, 'w') as json_file:
    for item in data:
        json.dump(item, json_file)
        json_file.write('\n')