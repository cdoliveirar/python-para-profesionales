'''
Al trabajar con diccionarios, a menudo es necesario acceder a todas las claves y valores en el diccionario, ya sea
en un bucle for, una comprensión de lista, o simplemente como una lista normal.
'''

mydict = {'a': '1', 'b': '2'}
# Puedes obtener una lista de claves usando el método keys():
print(mydict.keys())
# Si en cambio quieres una lista de valores, usa el método values():
print(mydict.values())
# Si deseas trabajar con tanto la clave como su valor correspondiente, puedes usar el método items():
print(mydict.items())

'''
NOTA: Debido a que un diccionario no está ordenado, keys(), values() e items() no tienen un orden específico. 
Usa sort(), sorted() o un OrderedDict si te importa el orden en que estos métodos devuelven los elementos.
'''






