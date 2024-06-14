'''
Recuperar datos de un archivo
'''

''' El siguiente fragmento de código abre un archivo codificado en JSON (reemplace filename con el nombre real del 
archivo) y devuelve el objeto que está almacenado en el archivo.'''

import json
with open("jsonfile.txt", 'r') as f:
    d = json.load(f)
    print(d)