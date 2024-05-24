'''
Las list comprehensions en Python son construcciones sintácticas concisas. Pueden ser utilizadas para generar listas a
partir de otras listas aplicando funciones a cada elemento en la lista. La siguiente sección explica y demuestra
el uso de estas expresiones.
'''

'''
Una list comprehension crea una nueva lista aplicando una expresión a cada elemento de un iterable. 
La forma más básica es:

[ <expression> for <element> in <iterable> ]

También hay una condición opcional 'if':

[ <expression> for <element> in <iterable> if <condition> ]

Cada <element> en el <iterable> se inserta en la <expression> si la (opcional) <condición> se evalúa como verdadera. 
Todos los resultados se devuelven de una vez en la nueva lista. Las expresiones generadoras se evalúan de forma 
perezosa(lazily), pero las list comprehensions evalúan todo el iterador inmediatamente, consumiendo memoria proporcional 
a la longitud del iterador
'''

''' Para crear una lista de enteros al cuadrado '''

squares = [x * x for x in (1, 2, 3, 4)]
print(squares)

''' La expresión for asigna a x cada valor sucesivamente de (1, 2, 3, 4). El resultado de la expresión x * x se 
agrega a una lista interna. La lista interna se asigna a la variable squares cuando se completa. '''

''' Además de un aumento de velocidad (como se explica aquí), una list comprehension es aproximadamente equivalente al 
siguiente bucle for'''

squares = []
for x in (1, 2, 3, 4):
    squares.append(x * x)
print(squares)

''' La expresión aplicada a cada elemento puede ser tan compleja como sea necesario.'''

# Obtener una lista de caracteres en mayúsculas a partir de una cadena
print([s.upper() for s in "Hello World"])       # ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# Eliminar las comas del final de las cadenas en una lista.
print([w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']])

# Organizar las letras en las palabras de manera más razonable, en orden alfabético
sentence = "Beautiful is better than ugly"
print(["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()])


''' 
else 

else puede ser utilizado en las construcciones de List comprehensions, pero ten cuidado con la sintaxis. Las cláusulas 
if/else deben usarse antes del bucle for, no después.
'''

# Crear una lista de caracteres en "apple", reemplazando las consonantes con '*'
# 'apple'  --> ['a', '*', '*', '*' ,'e']

# print([x for x in 'apple' if x in 'aeiou' else '*'])        # SyntaxError: invalid syntax

# Al usar if/else juntos, úsalos antes del bucle
print([x if x in 'aeiou' else '*' for x in 'apple'])        # ['a', '*', '*', '*', 'e']

''' Nota que esto utiliza una construcción de lenguaje diferente, una expresión condicional, que en sí misma no es 
parte de la sintaxis de las comprehensions. Mientras que el if después del for…in es parte de las list comprehensions 
y se utiliza para filtrar elementos del iterable fuente.'''

''' Doble Iteración.
El orden de la doble iteración [..., for x in ..., for y in ...] puede ser natural o contraintuitivo. La regla general 
es seguir un bucle for equivalente:
'''

def foo(i):
    return i, i + 0.5

def funcion_generadora():
    for i in range(3):
        for x in foo(i):
            yield str(x)
    # 0
    # 0.5
    # 1
    # 1.5
    # 2
    # 2.5

for item in funcion_generadora():
    print(item)

# esto se transforma en:
[str(x)
    for i in range(3)
        for x in foo(i)
]

# Esto puede ser comprimido en una sola line como:
print([str(x) for i in range(3) for x in foo(i)])
# ['0', '0.5', '1', '1.5', '2', '2.5']

''' Mutación In-place y Otros Efectos Secundarios

Antes de usar las list comprehensions, es importante entender la diferencia entre las funciones llamadas por sus 
efectos secundarios (mutantes, o funciones In-place) que usualmente devuelven None, y las funciones que devuelven 
un valor interesante.

Muchas funciones (especialmente las funciones puras) simplemente toman un objeto y devuelven algún objeto. Una función 
in-place modifica el objeto existente, lo que se llama un efecto secundario. Otros ejemplos incluyen operaciones de 
entrada y salida, como imprimir.

list.sort() ordena una lista en el lugar (lo que significa que modifica la lista original) y devuelve el valor None. 
Por lo tanto, no funcionará como se espera en una list comprehension
'''

print([x.sort() for x in [[2, 1], [4, 3], [0, 1]]])         # [None, None, None]

''' En su lugar, sorted() devuelve una lista ordenada en lugar de ordenar in-place: '''

print([sorted(x) for x in [[2, 1], [4, 3], [0, 1]]])        # [[1, 2], [3, 4], [0, 1]]


''' Usar comprehensions para efectos secundarios es posible, como en I/O o funciones in-place. Sin embargo, 
un bucle for suele ser más legible.
'''

[print(x) for x in (1, 2, 3)]

# en ves usa:
for x in (1, 2, 3):
    print(x)

''' En algunas situaciones, las funciones con efectos secundarios son adecuadas para las list comprehensions. 
random.randrange() tiene el efecto secundario de cambiar el estado del generador de números aleatorios, pero también 
devuelve un valor interesante. Además, se puede llamar a next() en un iterador.'''

'''
El siguiente generador de valores aleatorios no es puro, pero tiene sentido ya que el generador de números aleatorios 
se reinicia cada vez que se evalúa la expresión:
'''
from random import randrange
print([randrange(1, 7) for _ in range(10)])

''' 
Espacios en blanco en las list comprehensions

Las list comprehensions más complicadas pueden alcanzar una longitud indeseada o volverse menos legibles. Aunque es 
menos común en los ejemplos, es posible dividir una list comprehension en múltiples líneas de la siguiente manera

[
    x for x
    in 'foo'
    if x not in 'bar'
]
'''


