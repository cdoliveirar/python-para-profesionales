'''
Comprensiones que involucran tuplas.
'''

print([x + y for x, y in [(1, 2), (3, 4), (5, 6)]])         # [3, 7, 11]

print([x + y for x, y in zip([1, 3, 5], [2, 4, 6])])        # [3, 7, 11]

# Esto es igual que los bucles for regulares.
for x, y in [(1,2), (3,4), (5,6)]:
    print(x+y)

''' Sin embargo, ten en cuenta que si la expresión que comienza la comprensión es una tupla, debe estar entre 
paréntesis.'''
# print([x, y for x, y in [(1, 2), (3, 4), (5, 6)]])     # SyntaxError: invalid syntax

print([(x, y) for x, y in [(1, 2), (3, 4), (5, 6)]])        # [(1, 2), (3, 4), (5, 6)]