'''
Creado Json desde un diccionario Python
'''

import json
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

print(json.dumps(d))

# El fragmento anterior devolverá lo siguiente

#   {"foo": "bar", "alice": 1, "wonderland": [1, 2, 3]}