'''
Cualquier y Todo

Puedes usar all() para determinar si TODOS los valores en un iterable evalúan a True.
'''

nums = [1, 1, 0, 1]
print(all(nums))        # False

chars = ['a', 'b', 'c', 'd']
print(all(chars))       # True

''' De igual manera, any() determina si UNO O MÁS valores en un iterable evalúan a True '''
nums = [1, 1, 0, 1]
print(any(nums))        # True

vals = [None, None, None, False]
print(any(vals))        # Falsa

vals = [1, 2, 3, 4]
print(any(val > 12 for val in vals))        # False
print(any((val * 2) > 6 for val in vals))   # True

