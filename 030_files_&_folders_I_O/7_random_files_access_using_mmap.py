'''
Acceso Aleatorio a Archivos Usando mmap
'''

''' El uso del módulo mmap permite al usuario acceder aleatoriamente a ubicaciones en un archivo al mapear el archivo 
en la memoria. Esta es una alternativa al uso de operaciones normales de archivos.'''

import mmap

with open('filename.ext', 'r+') as fd:
    # 0: mapea todo el archivo
    mm = mmap.mmap(fd.fileno(), 0)

    # imprime los caracteres en los índices del 5 al 10
    print(mm[5:10])

    # imprime la línea comenzando desde la posición actual de mm
    print(mm.readline())

    # escribe un carácter en el índice 5
    mm[5] = 5

    # devuelve la posición de mm al principio del archivo
    mm.seek(0)

    # cierra el objeto mmap
    mm.close()
