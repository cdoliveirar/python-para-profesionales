'''
Desplazando una lista usando slicing
'''

def shift_list(array, s):
    """Shifts the elements of a list to the left or right.
    Args:
        array - the list to shift
        s - the amount to shift the list ('+': right-shift, '-': left-shift)
    Returns:
        shifted_array - the shifted list
    """

    # Calcula la cantidad real de desplazamiento (por ejemplo, 11 --> 1 si la longitud del arreglo es 5)
    s %= len(array)

    # Invierte la dirección del desplazamiento para que sea más intuitivo
    s *= -1
    # Desplaza el arreglo con slicing de listas
    shifted_array = array[s:] + array[:s]

    return shifted_array

my_array = [1, 2, 3, 4, 5]

# numero negativos
print(shift_list(my_array, -7))       # [3, 4, 5, 1, 2]

print(shift_list(my_array, 5))      # [1, 2, 3, 4, 5]

print(shift_list(my_array, 3))      # [3, 4, 5, 1, 2]


''' 
Desplazamiento Circular en Diferentes Contextos

Aplicación en algoritmos:

- Puedes utilizar el desplazamiento circular para implementar algoritmos de cifrado, donde cada carácter se desplaza 
una cierta cantidad de posiciones en una lista de caracteres.

- También es útil en problemas de programación competitiva donde se necesita manipular secuencias de datos de manera 
eficiente.

Animaciones o Visualizaciones:

- En aplicaciones gráficas o juegos, puedes usar el desplazamiento circular para crear efectos de animación continua.

Manejo de Colas (Queues):

- En estructuras de datos como colas circulares, el desplazamiento puede ayudar a gestionar el acceso a los elementos 
de manera cíclica.

'''