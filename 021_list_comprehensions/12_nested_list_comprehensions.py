'''
Comprensiones de listas anidadas

Las comprensiones de listas anidadas, a diferencia de las comprensiones de listas con bucles anidados, son
comprensiones de listas dentro de una comprensión de lista. La expresión inicial puede ser cualquier expresión
arbitraria, incluida otra comprensión de lista.
'''

#List Comprehension con bucles anidados
print([x + y for x in [1, 2, 3] for y in [3, 4, 5]])
#  [4, 5, 6, 5, 6, 7, 6, 7, 8]

# Comprensión de lista anidada.
print([[x + y for x in [1, 2, 3]] for y in [3, 4, 5]])
#  [[4, 5, 6], [5, 6, 7], [6, 7, 8]]

# el anidado ejemplo es equivalente a
l = []
for y in [3, 4, 5]:
    temp = []
    for x in [1, 2, 3]:
        temp.append(x + y)
    l.append(temp)


matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]

print([[row[i] for row in matrix] for i in range(len(matrix))])     # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

''' Al igual que con los bucles for anidados, no hay límite en cuán profundas pueden ser anidadas las comprensiones.'''

print([[[i + j + k for k in 'cd'] for j in 'ab'] for i in '12'])
#   [[['1ac', '1ad'], ['1bc', '1bd']], [['2ac', '2ad'], ['2bc', '2bd']]]