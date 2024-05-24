'''
Comprensión de Diccionario

Una comprensión de diccionario es similar a una comprensión de listas, excepto que produce un objeto diccionario en
lugar de una lista.
'''

print({x: x * x for x in (1, 2, 3, 4)})         # {1: 1, 2: 4, 3: 9, 4: 16}

# Que es solo otra forma de escribir:
print(dict((x, x * x) for x in (1, 2, 3, 4)))   # {1: 1, 2: 4, 3: 9, 4: 16}

''' Al igual que con una comprensión de listas, podemos usar una declaración condicional dentro de la comprensión de 
diccionario para producir solo los elementos del diccionario que cumplan con algún criterio.'''

print({name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6})
    # {'Overflow': 8, 'Exchange': 8}

''' O, reescrito usando una expresión generadora.'''

print(dict((name, len(name)) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6))
    # {'Overflow': 8, 'Exchange': 8}


'''  Comenzando con un diccionario y usando una comprensión de diccionario como filtro de pares clave-valor '''

initial_dict = {'x': 1, 'y': 2}
print({key: value for key, value in initial_dict.items() if key == 'x'})        # {'x': 1}



''' Intercambiar clave y valor del diccionario (invertir el diccionario)

Si tienes un diccionario que contiene valores hashables simples (valores duplicados pueden tener resultados inesperados) 
'''
my_dict = {1: 'a', 2: 'b', 3: 'c'}

''' y quieres intercambiar las claves y los valores, puedes tomar varios enfoques dependiendo de tu estilo de 
codificación.'''


swapped = {v: k for k, v in my_dict.items()}            # {'a': 1, 'b': 2, 'c': 3}
print(swapped)
swapped = dict(zip(my_dict.values(), my_dict))          # {'a': 1, 'b': 2, 'c': 3}, # puedes usar my_dict directamente
                                                                                    # para iterar sobre las claves del
                                                                                    # diccionario sin necesidad de llamar
                                                                                    # explícitamente a keys()
print(swapped)
swapped = dict(zip(my_dict.values(), my_dict.keys()))
    # {'a': 1, 'b': 2, 'c': 3}  # puedes llamar explicitamente a keys()
print(swapped)
swapped = dict(map(reversed, my_dict.items()))          # {'a': 1, 'b': 2, 'c': 3}
print(swapped)


''' Merging Dictionaries , Combinar diccionarios
combinar diccionarios y, opcionalmente, sobrescribir valores antiguos con una comprensión de diccionario anidada.
'''
dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}

print({k: v for d in [dict1, dict2] for k, v in d.items()})     # {'w': 1, 'x': 2, 'y': 2, 'z': 2}

# Si hay claves comunes entre dict1 y dict2, el valor correspondiente de dict2 sobrescribirá el valor de dict1, por eso
# 'x': 1 del dict1 ya no se muestra en la lista final combinada.

print({**dict1, **dict2})   # {'w': 1, 'x': 2, 'y': 2, 'z': 2}