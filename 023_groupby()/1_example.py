'''

Parametros              Details
iterable                Cualquier iterable de Python
key                     Función(criterio) sobre la cual agrupar el iterable


En Python, el método itertools.groupby() permite a los desarrolladores agrupar los valores de una clase iterable
basándose en una propiedad específica en otro conjunto iterable de valores.
'''

from itertools import groupby
'''
groupby es una función que agrupa elementos consecutivos de un iterable que tienen una clave en común
'''

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]

dic = {}
f = lambda x: x[0]
for key, group in groupby(sorted(things, key=f), f):
    group_list = list(group)
    print(str(key), group_list)
    dic[key] = group_list
print(dic)

# {'animal': [('animal', 'bear'), ('animal', 'duck')],
# 'plant': [('plant', 'cactus')],
# 'vehicle': [('vehicle', 'harley'), ('vehicle', 'speed boat'), ('vehicle', 'school bus')]}

'''  El objeto group es un generador, y una vez que lo consumes (como en la llamada a list(group) en el print), 
ya no puede ser iterado de nuevo.'''


''' Este ejemplo a continuación es esencialmente el mismo que el anterior. La única diferencia es que he cambiado todas 
las tuplas por listas.'''

things = [["animal", "bear"], ["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"], \
["vehicle", "speed boat"], ["vehicle", "school bus"]]

dic = {}
f = lambda x: x[0]
for key, group in groupby(sorted(things, key=f), f):
    dic[key] = list(group)
print(dic)

# {'animal': [['animal', 'bear'], ['animal', 'duck']],
# 'plant': [['plant', 'cactus']],
# 'vehicle': [['vehicle', 'harley'], ['vehicle', 'speed boat'], ['vehicle', 'school bus']]
# }

