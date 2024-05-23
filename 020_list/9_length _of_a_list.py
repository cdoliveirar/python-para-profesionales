'''
Longitud de una lista

Utiliza len() para obtener la longitud unidimensional de una lista.
'''

print(len(['one', 'two']))          # 2
print(len(['one', [2, 3], 'four']))     # 3


'''
len() también funciona con cadenas, diccionarios y otras estructuras de datos similares a las listas.

Ten en cuenta que len() es una función incorporada(built-in), no un método de un objeto lista.

También ten en cuenta que el costo de len() es O(1), lo que significa que tomará la misma cantidad de tiempo obtener 
la longitud de una lista sin importar su longitud.
'''