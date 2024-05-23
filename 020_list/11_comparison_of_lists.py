'''
Es posible comparar listas y otras secuencias lexicográficamente utilizando operadores de comparación. Ambos operandos
deben ser del mismo tipo.
'''

print([1, 10, 100] < [2, 10, 100])      # True

print([1, 10, 100] < [1, 10, 100])      # False

print([1, 10, 100] <= [1, 10, 100])     # True

print([1, 10, 100] < [1, 10, 101])      # True

print([1, 10, 100] < [0, 10, 100])      # False


''' Si una de las listas está contenida al inicio de la otra, la lista más corta gana. '''

print([1, 10] < [1, 10, 100])           # True