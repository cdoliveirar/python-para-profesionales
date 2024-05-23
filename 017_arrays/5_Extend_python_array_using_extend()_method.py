'''
Un array de Python puede ser extendido con más de un valor usando el método extend().
'''
from array import *

my_array = array('i', [1,2,3,4,5])
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array)

print(my_array)
# array('i', [1, 2, 3, 4, 5, 7, 8, 9, 10])
