'''
Iterar archivos (recursivamente)
'''

''' Para iterar sobre todos los archivos, incluidos  subdirectorios, utiliza os.walk '''

import os
for root, folders, files in os.walk("."):
    for filename in files:
        print(root, filename)

''' os.walk devuelve tres valores para cada directorio en el árbol de directorios:
* root: el nombre del directorio actual.
* folders: una lista de subdirectorios en el directorio actual.
* files: una lista de nombres de archivos en el directorio actual.
'''



''' Si también deseas obtener información sobre el archivo, puedes usar el método más eficiente os.scandir de la 
siguiente manera:'''

path=os.path.join(".")
for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file():
        print(entry.name)