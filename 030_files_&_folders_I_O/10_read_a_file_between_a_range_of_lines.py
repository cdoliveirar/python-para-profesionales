'''
Leer un archivo entre un rago de lineas
'''

''' Supongamos que deseas iterar solo entre algunas líneas específicas de un archivo. Puedes hacer uso de 
itertools para eso '''

import itertools
with open('myfile.txt', 'r') as f:
    for line in itertools.islice(f, 12, 30):
        pass # hacer algo por aqui

''' Esto leerá las líneas de la 13 a la 20, ya que en Python la indexación comienza desde 0. Así que la línea número 
1 está indexada como 0.
También puedes leer algunas líneas adicionales utilizando la palabra clave next() aquí.

Y cuando estés usando el objeto archivo como un iterable, por favor no usar la instrucción readline() aquí, 
ya que no se deben mezclar las dos técnicas de recorrer un archivo.'''

