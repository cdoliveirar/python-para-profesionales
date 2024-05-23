'''
Accediendo a valores en listas anidadas
'''

alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]

print(alist[0][0][1])   # 2 , Accede al segundo elemento en la primera lista dentro de la primera lista
print(alist[1][1][2])   # 10, Accede al tercer elemento en la segunda lista dentro de la segunda lista

# Realizando operaciones de soporte
alist[0][0].append(11)          # [[[1, 2, 11], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
print(alist)
print(alist[0][0][2])           # 11

''' Usando bucles for anidados para imprimir la lista. '''
for row in alist:       # One way to loop through nested lists
    for col in row:
        print(col)
        # [1, 2, 11]
        # [3, 4]
        # [5, 6, 7]
        # [8, 9, 10]
        # [12, 13, 14]


''' Ten en cuenta que esta operación se puede utilizar en una comprensión de listas o incluso como un generador 
para producir eficiencias.'''
print([col for row in alist for col in row])
# [[1, 2, 11], [3, 4], [5, 6, 7], [8, 9, 10], [12, 13, 14]]


''' No todos los elementos en las listas exteriores tienen que ser listas en sí mismos'''
alist[1].insert(2, 15)      # Inserta 15 en la tercera posición en la segunda lista.
print(alist)        # [[[1, 2, 11], [3, 4]], [[5, 6, 7], [8, 9, 10], 15, [12, 13, 14]]]

''' Otra forma de usar bucles for anidados. La otra forma es mejor, pero he necesitado usar esto en ocasiones '''
for row in range(len(alist)):   # Una forma menos pythonica de iterar a través de listas.
    for col in range(len(alist[row])):
        print(alist[row][col])

''' Usando Slices en listas anidadas '''

print(alist[1][1:])     # [[8, 9, 10], 15, [12, 13, 14]]

print(alist)        # [[[1, 2, 11], [3, 4]], [[5, 6, 7], [8, 9, 10], 15, [12, 13, 14]]]

