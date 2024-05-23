'''
LIST
----
La lista de Python es una estructura de datos general ampliamente utilizada en programas de Python. Se encuentran
en otros lenguajes, a menudo referidos como arreglos dinámicos. Son tanto mutables como un tipo de datos de secuencia
que les permite ser indexados y cortados. La lista puede contener diferentes tipos de objetos, incluyendo otros objetos
de lista.
'''

# Comenzando con una lista dada a
a = [1, 2, 3, 4, 5]

'''
1. append(value) – añade un nuevo elemento al final de la lista.
'''
a.append(6)
a.append(7)
a.append(8)
print(a)        # [1, 2, 3, 4, 5, 6, 7, 8]

# Añade otra lista
b = [8, 9]
a.append(b)
print(a)        # [1, 2, 3, 4, 5, 6, 7, 8, [8, 9]]

# Añade un elemento de un tipo diferente, ya que los elementos de la lista no necesitan tener el mismo tipo.
my_string = "hello world"
a.append(my_string)
print(a)        # [1, 2, 3, 4, 5, 6, 7, 8, [8, 9], 'hello world']

# Ten en cuenta que el método append() solo añade un nuevo elemento al final de la lista. Si añades una lista a otra
# lista, la lista que añades se convierte en un único elemento al final de la primera lista.

a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9]
a.append(b)
print(a[8])     # [8, 9]

'''
2. extend(enumerable) – añade un nuevo elemento al final de la lista.
'''
a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9, 10]
# Extiende la lista añadiendo todos los elementos de b.
a.extend(b)
print(a)        # [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

# Extender la lista con elementos de un objeto enumerable que no es una lista
a.extend(range(3))
print(a)        # [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 0, 1, 2]

# Las listas también pueden ser concatenadas con el operador +. Ten en cuenta que esto no modifica ninguna de las
# listas originales.
a = [1, 2, 3, 4, 5, 6] + [7, 7] + b
print(a)        # [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]


'''
3. index(value, [startIndex]) - obtiene el índice de la primera ocurrencia del valor de entrada. Si el valor de 
entrada no está en la lista, se genera una excepción ValueError. Si se proporciona un segundo argumento, la búsqueda 
comienza en ese índice especificado.
'''
print(a.index(7))       # 6
# print(a.index(49))      # ValueError: 49 is not in list

print(a.index(7, 7))    # 7
# print(a.index(7, 8))    # ValueError, porque no hay un 7 comenzando desde el índice 8.


'''
4. insert(index, value) - Inserta el valor justo antes del índice especificado. Por lo tanto, después de la inserción, 
el nuevo elemento ocupa la posición del índice.
'''
a.insert(0, 0)  # Inserta 0 en la posision 0
# [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
print(a)

a.insert(2, 5)  # Inserta 5 en la posision 2
# [0, 1, 5, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
print(a)

'''
5. pop([index]) - Elimina y devuelve el elemento en el índice especificado. Sin argumentos, elimina y devuelve el 
último elemento de la lista.
'''
# Con argumento
print(a.pop(2))     # 5, elemento en el indice 2  especificado.
print(a.pop(8))     # 7, elemento en el indice 8  especificado.
print(a)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sin argumentos
print(a.pop())      # 10, ultimo elemento de la lista
print(a)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
6. remove(value)  - Elimina la primera ocurrencia del valor especificado. Si no se puede encontrar el valor 
proporcionado, se genera un ValueError
'''

a.remove(0)
a.remove(9)
print(a)        # [1, 2, 3, 4, 5, 6, 7, 8]
# a.remove(10)    # ValueError: list.remove(x): x not in list

'''
7. reverse() - Invierte la lista en su lugar y devuelve None.
'''

a.reverse()
print(a)    # [8, 7, 6, 5, 4, 3, 2, 1]

'''
8. count(value) - Cuenta el número de ocurrencias de un valor en la lista.
'''

print(a.count(7))   # devuelve 1

'''
9. sort() - Ordena la lista en orden numérico y lexicográfico y devuelve None.
'''

a.sort()
print(a)    # [1, 2, 3, 4, 5, 6, 7, 8] , Ordena la lista en un orden numérico

# Si deseas ordenar por atributos de los elementos, puedes usar el argumento de palabra clave 'key'.

import datetime
class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name


l = [Person("John Cena", datetime.date(1992, 9, 12), 175),
     Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
     Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]

l.sort(key=lambda item: item.name)      # [Chuck Norris, John Cena, Jon Skeet]
l.sort(key=lambda item: item.birthday)  # [Chuck Norris, Jon Skeet, John Cena]
l.sort(key=lambda item: item.height)    # [John Cena, Chuck Norris, Jon Skeet]
print(l)

# En caso de una lista de diccionarios, el concepto es el mismo
l = [{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),'height': 175},
{'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),'height': 180},
{'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'height': 185}]

l.sort(key=lambda item: item['name'])
print("Diccionarios: ")
print(l)
# Ordenados por Nombre (Name)
nombres_ordenados = sorted([d['name'] for d in l])
print(nombres_ordenados)        # ['Chuck Norris', 'John Cena', 'Jon Skeet']

# Ordenado por Cumpleaños (birthday)
l_sorted = sorted(l, key=lambda x: x['birthday'])
nombres_ordenados = [d['name'] for d in l_sorted]
print(nombres_ordenados)        # ['Chuck Norris', 'Jon Skeet', 'John Cena']

# Ordenado por Altura (height)
l_sorted = sorted(l, key=lambda x: x['height'])
nombres_ordenados = [d['name'] for d in l_sorted]
print(nombres_ordenados)        # ['John Cena', 'Chuck Norris', 'Jon Skeet']

# Ordenar por subdiccionario: (sub dict)
l = [{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),
      'size': {'height': 175,'weight': 100}
      },
    {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),
     'size' : {'height': 180,'weight': 90}
     },
    {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6),
     'size': {'height': 185,'weight': 110}
    }]

l.sort(key=lambda item: item['size']['height'])
print(l)

# Ordenar la lista por la altura de cada persona
l_sorted = sorted(l, key=lambda x: x['size']['height'])
# Extraer solo los nombres en el orden resultante
nombres_ordenados = [d['name'] for d in l_sorted]
print(nombres_ordenados)        # ['John Cena', 'Chuck Norris', 'Jon Skeet']


'''
Una mejor manera de ordenar usando attrgetter e itemgetter

Las listas también pueden ordenarse utilizando las funciones attrgetter e itemgetter del módulo operator. Estas pueden 
ayudar a mejorar la legibilidad y la reutilización.
'''

from operator import itemgetter,attrgetter

people = [{'name':'chandan','age':20,'salary':2000},
          {'name':'chetan','age':18,'salary':5000},
          {'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')

people.sort(key=by_age)
print(people)
people.sort(key=by_salary)
print(people)

# También se le puede proporcionar un índice a itemgetter. Esto es útil si deseas ordenar basado en los índices
# de una tupla.
list_of_tuples = [(1,2), (3,4), (5,0)]
list_of_tuples.sort(key=itemgetter(1))  # Va ordenar por el indice 1 ne la tupla, entonces: 0, 2, 4,
print(list_of_tuples)       # [(5, 0), (1, 2), (3, 4)]

'''
Usa attrgetter si quieres ordenar por atributos de un OBJETO,
'''
persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),
           Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
           Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]
persons.sort(key=attrgetter('name'))
print(persons)

by_birthday = attrgetter('birthday')
persons.sort(key=by_birthday)
print(persons)


'''
10. clear() – Elimina todos los elementos de la lista
'''
print(a)    # [1, 2, 3, 4, 5, 6, 7, 8]
a.clear()
print(a)    # []


'''
11. Replication – Multiplicar una lista existente por un entero producirá una lista más grande que consiste en tantas 
copias del original. Esto puede ser útil, por ejemplo, para la inicialización de listas.
'''
b = ["blah"] * 3
print(b)
b = [1, 3, 5] * 5
print(b)

'''
Toma precauciones al hacer esto si tu lista contiene referencias a objetos (por ejemplo, una lista de listas). 
Consulta 'Pitfalls comunes - Multiplicación de listas y referencias comunes'
'''


'''
12. Element deletion – Es posible eliminar varios elementos en la lista usando la palabra clave del y la notación 
slicing.
'''

a = list(range(10))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[::2]              # [1, 3, 5, 7, 9]
del a[-1]               # [1, 3, 5, 7]
del a[:]                # []


'''
13. Copying - La asignación predeterminada '=' asigna una referencia de la lista original al nuevo nombre. Es decir, 
tanto el nombre original como el nuevo nombre apuntan al mismo objeto de lista. Los cambios realizados a través de 
cualquiera de ellos se reflejarán en el otro. Esto a menudo no es lo se pretende.  
'''

a = list(range(4))
b = a
a.append(6)
print(b)

''' Si quieres crear una copia de la lista, tienes las siguientes opciones..'''

''' Puedes cortarla
    new_list = old_list[:]
'''

''' Puedes usar la función incorporada (built in) list():
    new_list = list(old_list)
'''

''' Puedes usar copy.copy() genérico.
    import copy
    new_list = copy.copy(old_list) # inserta referencias a los objetos encontrados en el original
    
    Esto es un poco más lento que list() porque primero tiene que determinar el tipo de datos de old_list. Si la lista 
    contiene objetos y quieres copiarlos también, usa copy.deepcopy() genérico
    
    import copy
    new_list = copy.deepcopy(old_list) # inserta copias de los objetos encontrados en el original.
    
    Obviamente, el método más lento y que necesita más memoria, pero a veces inevitable
'''

# copy() - Devuelve una copia superficial de la lista.
aa = a.copy()
a.append(6100)
print(aa)
print(a)