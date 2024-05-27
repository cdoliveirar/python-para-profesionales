'''
Invirtiendo una lista con slicing
'''

a = [1, 2, 3, 4, 5]
# recorre la lista hacia atrás (paso = -1)

b = a[::-1]
# método incorporado de lista para invertir 'a'

a.reverse()
if a == b:
    print(True)     # True
print(b)            # # [5, 4, 3, 2, 1]

