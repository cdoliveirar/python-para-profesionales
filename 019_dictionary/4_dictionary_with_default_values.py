'''
Disponible en la biblioteca standar como defaultdict
'''
from collections import defaultdict

d = defaultdict(int)
print(d['key'])         # 0
d['key'] = 5
print(d['key'])         # 5

d = defaultdict(lambda: 'empty')
print(d['key'])         # 'empty'
d['key'] = 'full'
print(d['key'])         # 'full'

'''
[*] Alternativamente, si debes usar la clase de diccionario incorporada, el uso de dict.setdefault() te permitirá 
crear un valor predeterminado siempre que accedas a una clave que no existía antes.
'''
d = {}
d.setdefault('Another_key', []).append("This worked!")
print(d)            # {'Another_key': ['This worked!']}

'''
Ten en cuenta que si tienes muchos valores que agregar, dict.setdefault() creará una nueva instancia del valor inicial 
(en este ejemplo, un []) cada vez que se llame, lo que podría generar cargas de trabajo innecesarias.
'''
