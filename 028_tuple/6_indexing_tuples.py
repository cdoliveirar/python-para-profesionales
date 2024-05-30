'''
Indexación de tuplas
'''

x = (1,2,3)
print(x[0])     #   1
print(x[1])     #   2
print(x[2])     #   3
# print(x[3])     # IndexError: tuple index out of range

''' La indexación con números negativos comenzará desde el último elemento como -1'''
print(x[-1])    # 3
print(x[-2])    # 2
print(x[-3])    # 1
# x[-4]       # IndexError: tuple index out of range

''' Indexando rango de elementos'''
print(x[:-1])
print(x[-1:])   # empezar desde el último elemento (debido al índice negativo -1) y continuar hasta el final de la tupla
print(x[1:3])

