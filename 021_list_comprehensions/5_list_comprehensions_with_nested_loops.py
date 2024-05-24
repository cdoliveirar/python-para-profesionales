'''
Comprensiones de listas con bucles anidados

Las Comprensiones de Listas pueden usar bucles for anidados. Puedes codificar cualquier cantidad de bucles for anidados
dentro de una comprensión de lista, y cada bucle for puede tener una prueba if opcional asociada. Al hacerlo,
el orden de los constructos for es el mismo orden que al escribir una serie de declaraciones for anidadas.
La estructura general de las comprensiones de lista se ve así

[ expression for target1 in iterable1 [if condition1]
            for target2 in iterable2 [if condition2]...
            for targetN in iterableN [if conditionN] ]

'''

# El siguiente código aplana(ﬂattening) una lista de listas usando múltiples declaraciones for
data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
print(output)       # [1, 2, 3, 4, 5, 6]

''' Puede escribirse de manera equivalente como una comprensión de lista con múltiples constructos for'''
data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]
print(output)       # [1, 2, 3, 4, 5, 6]

''' Las declaraciones if en línea están anidadas de manera similar, y pueden ocurrir en cualquier posición después 
del primer for'''

data = [[1], [2, 3], [4, 5]]
output = [element for each_list in data
            if len(each_list) == 2
            for element in each_list
            if element != 5]
print(output)           # [2, 3, 4]


''' Por el bien de la legibilidad, sin embargo, deberías considerar el uso de bucles for tradicionales. Esto es 
especialmente cierto cuando la anidación es de más de 2 niveles de profundidad y/o la lógica de la comprensión es 
demasiado compleja. La comprensión de listas con múltiples bucles anidados podría propiciar errores o producir 
resultados inesperados.'''