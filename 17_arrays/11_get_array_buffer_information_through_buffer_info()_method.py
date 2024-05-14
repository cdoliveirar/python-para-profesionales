'''
Obtener información del búfer del array a través del método buffer_info().

Este método te proporciona la dirección de inicio del búfer del array en memoria y el número de elementos en el array.
'''
from array import *

my_array = array('i', [1,2,3,4,5])
my_array.buffer_info()
print(my_array.buffer_info())

# 140025453787856, 5)

