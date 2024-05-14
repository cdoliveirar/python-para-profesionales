'''
El método reverse() hace lo que su nombre indica: invierte el orden del array.
'''
from array import *

my_array = array('i', [1,2,3,4,5])
my_array.reverse()
print(my_array)
# array('i', [5, 4, 3, 2, 1])