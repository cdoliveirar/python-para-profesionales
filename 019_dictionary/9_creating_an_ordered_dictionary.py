'''
Puedes crear un diccionario ordenado que seguirá un orden determinado al iterar sobre las claves del diccionario

Usa OrderedDict del módulo collections. Esto siempre devolverá los elementos del diccionario en el orden original
de inserción cuando se itere sobre ellos
'''

from collections import OrderedDict
d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4

for key in d:
    print(key, d[key])      # "first 1", "second 2", "third 3", "last 4"