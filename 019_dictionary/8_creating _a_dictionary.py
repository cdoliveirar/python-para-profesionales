'''
Reglas para crear un diccionario:
- Cada clave debe ser única (de lo contrario, será sobrescrita).
- Cada clave debe ser hashable (se puede usar la función hash para hashearla; de lo contrario, se lanzará un TypeError).
- No hay un orden particular para las claves.
'''

# Crear y poblarlo con valores.
stock = {'eggs': 5, 'milk': 2}

# O creado un diccionario vacio
dictionary = {}

# Y poblarlo después.
dictionary['eggs'] = 5
dictionary['milk'] = 2

# Los valores tambien pueden ser listas
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
print(mydict['a'])

# Usa el método list.append() para agregar nuevos elementos a la lista de valores.
mydict['a'].append(4)
print(mydict['a'])
mydict['b'].append('four')
print(mydict['b'])

# También podemos crear un diccionario usando una lista de tuplas de dos elementos.
iterable = [('eggs', 5), ('milk', 2)]
dictionary = dict(iterable)
print(dictionary)

# O usando argumentos de palabra clave
dictionary = dict(eggs=5, milk=2)
print(dictionary)

# Otra forma es usar dict.fromkeys:
dictionary = dict.fromkeys(('milk', 'eggs'))
print(dictionary)       # {'milk': None, 'eggs': None}
dictionary = dict.fromkeys(('milk', 'eggs'), (2, 5))
print(dictionary)       # {'milk': (2, 5), 'eggs': (2, 5)}
