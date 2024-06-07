'''
Verificar solo un elemento en un iterable
'''

''' Utiliza el desempaquetado para extraer el primer elemento y asegurarte de que sea el único.'''

a, = {1,} # iterable

def foo():
    yield 1
a, = foo()      # a = 1

nums = [1, 2, 3]
a, = nums   # ValueError: too many values to unpack

