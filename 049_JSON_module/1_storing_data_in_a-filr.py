'''
Almacenando datos en un archivo
'''

''' El siguiente fragmento codifica los datos almacenados en d en JSON y los guarda en un archivo (reemplaza filename 
por el nombre real del archivo). python'''

import json

d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

with open("jsonfile.txt", 'w') as f:
    json.dump(d, f)     # Convierte dict a json

