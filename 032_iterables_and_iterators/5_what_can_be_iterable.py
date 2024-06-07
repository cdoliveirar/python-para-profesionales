'''
¿Qué puede ser iterable?
'''

''' Iterable puede ser cualquier cosa para la cual se reciben elementos uno por uno, solo hacia adelante. Las 
colecciones integradas de Python son iterables.'''

[1,2,3]         # list, iterar sobre los elementos
(1,2,3)         # tupla,
{1,2,3}         # set,
{1:2, 3:4}      # dict, terar sobre las claves(keys)


''' Los generadores devuelven iterables.'''

def foo():      # foo aún no es iterable...
    yield 1
res = foo()     # ...pero res ya lo es

''' Cuando defines la función foo() con la palabra clave yield, esta función se convierte en un generador. Sin embargo, 
foo() en sí misma no es iterable hasta que la llamas. Al llamar a foo() y asignar su resultado a res, res se convierte 
en un objeto generador, que es iterable. Por lo tanto, res ya es iterable.'''


