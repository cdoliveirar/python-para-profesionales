'''
Este ejemplo ilustra cómo se elige la clave predeterminada si no especificamos ninguna.
'''
from itertools import groupby

c = groupby(['goat', 'dog', 'cow', 1,1,1,1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

# {
# 'goat': ['goat'],
# 'dog': ['dog'],
# 'cow': ['cow'],
# 1: [1, 1, 1, 1, 1],
# 2: [2], 3: [3], 11: [11],
# 10: [10], ('persons', 'man', 'woman'): [('persons', 'man', 'woman')]
# }

''' Observa que aquí la tupla en su totalidad cuenta como una sola clave en esta lista. '''