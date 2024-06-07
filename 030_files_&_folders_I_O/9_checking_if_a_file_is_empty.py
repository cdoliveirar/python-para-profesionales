'''
Validando si un archivo esta vacio
'''
import os
os.stat("path_to_file").st_size == 0

# ó

import os
os.path.getsize("path_to_file") > 0

''' Sin embargo, ambos lanzarán una excepción si el archivo no existe. Para evitar tener que capturar tal error, 
haz esto:'''

import os
def is_empty_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

''' El cual retornara un valor booleano'''
