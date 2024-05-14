'''
Puedes agregar una cadena a un arreglo de caracteres utilizando fromstring().
'''

from array import *

my_char_array = array('c', ['g','e','e','k'])
my_char_array.fromstring("stuff")
print(my_char_array)

# metodo no soportado en python 3 !!