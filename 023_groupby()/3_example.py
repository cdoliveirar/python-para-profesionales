'''
Observa en este ejemplo que mulato y camel no aparecen en nuestro resultado. Solo el último elemento con la clave
especificada aparece. El último resultado para c en realidad elimina dos resultados anteriores. Pero observa la nueva
versión donde primero tengo los datos ordenados con la misma clave.
'''
from itertools import groupby

list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),'wombat', 'mongoose',
               'malloo', 'camel']

c = groupby(list_things, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

# {
# 'g': ['goat'],
# 'd': ['dog', 'donkey'],
# 'm': ['mongoose', 'malloo'],
# 'c': ['camel'],
# 'persons': [('persons', 'man', 'woman')],
# 'w': ['wombat']
# }

''' Sorted Version '''
print(''' Sorted Version '''  )
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),
               'wombat', 'mongoose', 'malloo', 'camel']

sorted_list = sorted(list_things, key = lambda x: x[0])
print(sorted_list)
print()
c = groupby(sorted_list, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

# {'c': ['cow', 'cat', 'camel'],
# 'd': ['dog', 'donkey'],
# 'g': ['goat'],
# 'm': ['mulato', 'mongoose', 'malloo'],
# 'persons': [('persons', 'man', 'woman')],
# 'w': ['wombat']
# }