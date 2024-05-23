'''
Podemos usar el método insert() para insertar un valor en cualquier índice del array.
'''
from array import *

my_array = array('i', [1,2,3,4,5])
my_array.insert(0,0)
print(my_array)
# array('i', [0, 1, 2, 3, 4, 5])


# En el ejemplo anterior, el valor 0 fue insertado en el índice 0. Observa que el primer argumento es el índice y el
# segundo argumento es el valor.

