'''
Creando Python diccionario desde Json
'''

import json
s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}'
print(json.loads(s))

# El fragmento de arriba retornará lo siguiente:
#   {'wonderland': [1, 2, 3], 'foo': 'bar', 'alice': 1}