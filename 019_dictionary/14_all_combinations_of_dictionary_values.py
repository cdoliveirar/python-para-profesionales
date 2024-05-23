options = {
"x": ["a", "b"],
"y": [10, 20, 30]
}

print(options)

'''
Dado un diccionario como el mostrado arriba, donde hay una lista representando un conjunto de valores para explorar 
para la clave correspondiente. Supongamos que quieres explorar "x"="a" con "y"=10 , luego "x"="a" con "y"=10 , 
y así sucesivamente hasta que hayas explorado todas las combinaciones posibles. 

Puedes crear una lista que devuelva todas esas combinaciones de valores usando el siguiente código.
'''

import itertools

options = {
"x": ["a", "b"],
"y": [10, 20, 30]}

keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
print(combinations)

# [{'x': 'a', 'y': 10},
# {'x': 'a', 'y': 20},
# {'x': 'a', 'y': 30},
# {'x': 'b', 'y': 10},
#  {'x': 'b', 'y': 20},
# {'x': 'b', 'y': 30}]