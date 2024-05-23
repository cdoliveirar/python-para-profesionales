'''
Eliminar valores duplicados en la lista

Eliminar los valores duplicados en una lista se puede hacer convirtiendo la lista en un set (que es una colección
desordenada de objetos distintos). Si se necesita una estructura de datos de lista, entonces el conjunto se puede
convertir nuevamente a una lista utilizando la función list():
'''

names = ["aixk", "duke", "edik", "tofp", "duke"]
print(list(set(names)))     # ['edik', 'aixk', 'tofp', 'duke']

'''
Ten en cuenta que al convertir una lista a un conjunto, el orden original se pierde.
Para preservar el orden de la lista, se puede usar un OrderedDict.
'''

import collections
print(collections.OrderedDict.fromkeys(names).keys())
# odict_keys(['aixk', 'duke', 'edik', 'tofp'])
