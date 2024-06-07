'''
Verificar si un archivo o ruta existe
'''

import errno

try:
    with open("path") as f:
        pass # el archivo existe


except IOError as e:
        # Lanza la excepción si no es ENOENT (No existe el archivo o directorio)
    if e.errno != errno.ENOENT:
        raise
# No such file or directory

''' Esto también evitará condiciones de carrera si otro proceso eliminó el archivo entre la verificación y el momento 
en que se utiliza. Esta condición de carrera podría ocurrir en los siguientes casos:'''

# Usando el os modulo
import os
os.path.isfile('/path/to/some/file.txt')

# usando pathlib
import pathlib

path = pathlib.Path('/path/to/some/file.txt')
if path.is_file():
    pass # ...


''' Para verificar si una ruta dada existe o no, puedes seguir el procedimiento EAFP mencionado anteriormente o 
verificar explícitamente la ruta.'''

import os
path = "/home/myFiles/directory1"
if os.path.exists(path):
    pass # Has cosas