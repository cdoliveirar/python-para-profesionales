'''
Función Map
'''

''' Map toma una función y una colección de elementos. Crea una nueva colección vacía, ejecuta la función en cada 
elemento de la colección original e inserta cada valor de retorno en la nueva colección. Devuelve la nueva colección.

Este es un simple map que toma una lista de nombres y devuelve una lista con las longitudes de esos nombres:'''

name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(list(name_lengths))       # [4, 4, 3]


