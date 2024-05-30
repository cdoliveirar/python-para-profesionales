'''
Empaquetar y Desempaquetar Tuplas

Las tuplas en Python son valores separados por comas. Los paréntesis para introducir tuplas son opcionales, por lo
que las dos asignaciones:
'''

a = 1, 2, 3         # es una tupla  (1, 2, 3)

a = (1, 2, 3)       # es una tupla  (1, 2, 3)

''' son equivalentes. La asignación a = 1, 2, 3 también se llama empaquetado (packing) porque empaqueta valores juntos 
en una tupla.
Ten en cuenta que una tupla de un solo valor también es una tupla. Para indicar a Python que una variable es una 
tupla y no un valor único, puedes usar una coma al final'''

a = 1           # a es el valor 1
a = 1,          # a es el valor tuple (1,)

''' También se necesita una coma si usas paréntesis '''

a = (1,)        # a es una tupla (1,)
a = (1)         # a es el valor 1 y no es una tupla

''' Para desempaquetar valores de una tupla y hacer múltiples asignaciones usa'''
# unpacking AKA multiple assignment
# desempaquetando tambien conocido como multiple asignacion
x, y, z = (1, 2, 3)
# x == 1
# y == 2
# z == 3

''' Tuplas de un solo elemento'''
x, = 1,         # x is the value 1
x = 1,          # x is the tuple (1,)


''' variable objetivo con un prefijo * se puede usar como una variable comodín '''
first, *more, last = (1, 2, 3, 4, 5)
# first == 1
# more == [2, 3, 4]
# last == 5
print(first)        # 1
print(*more)       # 2 3 4
print(more)         # [2, 3, 4]
print(last)         # 5
print(first, *more, last)
