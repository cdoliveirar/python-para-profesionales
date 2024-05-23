'''
El constructor dict() puede ser utilizado para crear diccionarios a partir de argumentos de palabras clave, o a
partir de un único iterable de pares clave-valor, o a partir de un solo diccionario y argumentos de palabras clave.
'''

print(dict(a=1, b=2, c=3))                      # {'a': 1, 'b': 2, 'c': 3}
print(dict([('d', 4), ('e', 5), ('f', 6)]))     # {'d': 4, 'e': 5, 'f': 6}
print(dict([('a', 1)], b=2, c=3))               # {'a': 1, 'b': 2, 'c': 3}
print(dict({'a' : 1, 'b' : 2}, c=3))            # {'a': 1, 'b': 2, 'c': 3}