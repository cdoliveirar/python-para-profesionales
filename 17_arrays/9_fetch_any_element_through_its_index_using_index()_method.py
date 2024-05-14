'''
Obtener cualquier elemento mediante su índice utilizando el método index().

El método index() devuelve el primer índice del valor coincidente. Recuerda que los arrays tienen índices que
comienzan desde cero.
'''
from array import *

my_array = array('i', [1,2,3,4,5])
print(my_array.index(5))
# 5
my_array = array('i', [1,2,3,3,5])
print(my_array.index(3))
# 3

# Nota que en el segundo ejemplo solo se devolvió un índice, aunque el valor exista dos veces en el array.