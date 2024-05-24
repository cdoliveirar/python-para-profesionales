'''
Cambiar Tipos en una Lista

Los datos cuantitativos a menudo se leen como cadenas que deben convertirse a tipos numéricos antes de procesarlos.
Los tipos de todos los elementos de una lista pueden convertirse con una Comprensión de Lista o la función map().
'''

# Convertir una list de strings a integers.
items = ["1","2","3","4"]
print([int(item) for item in items])        # [1, 2, 3, 4]

# Convertir una lista de string a float.
items = ["1","2","3","4"]
print(list(map(float, items)))              # [1.0, 2.0, 3.0, 4.0]
