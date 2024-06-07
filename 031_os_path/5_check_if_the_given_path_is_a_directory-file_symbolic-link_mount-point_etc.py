'''
verificar si la ruta dada es un directorio, archivo, enlace simbólico, punto de montaje, etc.
'''

import os


''' Para verificar si la ruta dada es un directorio'''
dirname = '/home/john/python'
print(os.path.isdir(dirname))       # False

''' Para verificar si la ruta dada es un archivo'''
filename = dirname + 'main.py'
print(os.path.isfile(filename))     # False

''' Para verificar si la ruta dada es un enlace simbolico'''
symlink = dirname + 'some_sym_link'
print(os.path.islink(symlink))      # False

''' Para verificar si la ruta dada es un punto de montaje'''
mount_path = '/home'
print(os.path.ismount(mount_path))  # True xD


