'''
Funciones integradas de tuplas

Las tuplas admiten las siguientes funciones integradas:
'''

'''
Comparación

Si los elementos son del mismo tipo, Python realiza la comparación y devuelve el resultado. Si los elementos son de 
tipos diferentes, se verifica si son números.
- Si son números, se realiza la comparación.
- Si uno de los elementos es un número, entonces se devuelve el otro elemento.
- De lo contrario, los tipos se ordenan alfabéticamente.
Si hemos alcanzado el final de una de las listas, la lista más larga es "mayor". Si ambas listas son iguales,devuelve 0.
'''

tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
tuple3 = ('a', 'b', 'c', 'd', 'e')

from functools import cmp_to_key

''' Tuple Length  
La funcion len retorna la total longitud de una tupla.
'''
len(tuple1)

print(len(tuple1))      # 5

''' Max de una tupla 
La función max devuelve el elemento de la tupla con el valor máximo.
'''
print(max(tuple1))      # e
print(max(tuple2))      # 3

''' Min de una tupla'''
print(min(tuple1))      # a
print(min(tuple2))      # 1

''' Convertir una lista en tupla'''
list = [1,2,3,4,5]
print(tuple(list))      # (1, 2, 3, 4, 5)

# puedes usar + para concatenar 2 tuplas.
print(tuple1 + tuple2)  # ('a', 'b', 'c', 'd', 'e', '1', '2', '3')