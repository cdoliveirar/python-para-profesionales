'''
ARRAYS
------
Parameter               Detalles
b               Representa un entero con signo de tamaño 1 byte.
B               Representa un entero sin signo de tamaño 1 byte.
c               Representa un carácter de tamaño 1 byte.
u               Representa un carácter unicode de tamaño 2 bytes.
h               Representa un entero con signo de tamaño 2 bytes.
H               Representa un entero sin signo de tamaño 2 bytes.
i               Representa un entero con signo de tamaño 2 bytes.
I               Representa un entero sin signo de tamaño 2 bytes.
w               Representa un carácter unicode de tamaño 4 bytes.
l               Representa un entero con signo de tamaño 4 bytes.
L               Representa un entero sin signo de tamaño 4 bytes.
f               Representa un punto flotante de tamaño 4 bytes
d               Representa un punto flotante de tamaño 8 bytes.


Los 'arrays' en Python no son los 'arrays' en lenguajes de programación convencionales como C y Java, sino más cercanos
a las listas. Una lista puede ser una colección de elementos homogéneos o heterogéneos, y puede contener enteros,
cadenas u otras listas
'''

'''
Los elementos individuales pueden ser accedidos a través de índices.
Los arrays en Python tienen índices comenzando desde cero.
'''
from array import *
my_array = array('i', [1,2,3,4,5])

print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



