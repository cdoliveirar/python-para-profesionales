'''
Si utilizas un diccionario como un iterador (por ejemplo, en una declaración for), recorre las claves del diccionario.
'''
d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])

# Lo mismo es válido cuando se utiliza en una comprensión.
print([key for key in d])

# El método items() se puede usar para iterar sobre tanto la clave como el valor simultáneamente:
# 1
print({k:v for k,v in d.items()})
# 2
for key, value in d.items():
    print(key, value)

# Mientras que el método values() puede ser usado para iterar sólo sobre los valores, como se esperaría.
# 1
print({v for v in d.values()})
# 2
for value in d.values():
    print(value)

'''
Aquí, los métodos keys(), values() e items() devuelven listas, y hay tres métodos adicionales iterkeys(), 
itervalues() e iteritems() para devolver iteradores.
'''