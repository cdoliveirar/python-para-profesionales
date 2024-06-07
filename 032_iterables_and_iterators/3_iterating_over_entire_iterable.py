'''
Iterando sobre todo el iterable
'''

s = {1, 2, 3}
# get every element in s
for a in s:
    print(a) # prints 1, then 2, then 3
# copiar a una lista
l1 = list(s) # l1 = [1, 2, 3]
# usar list comprehension
l2 = [a * 2 for a in s if a > 2]
print(l2)       # [6]
