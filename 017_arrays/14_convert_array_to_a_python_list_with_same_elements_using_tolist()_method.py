'''
Cuando necesites un objeto lista de Python, puedes utilizar el método tolist() para convertir tu arreglo en una lista.
'''

from array import *

my_array = array('i', [1,2,3,4,5])
c = my_array.tolist()

print(c)

# [1, 2, 3, 4, 5]