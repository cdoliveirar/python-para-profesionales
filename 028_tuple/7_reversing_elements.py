'''
Revertir elementos
'''

colors = "red", "green", "blue"
rev = colors[::-1]
colors = rev
print(colors)       # ('blue', 'green', 'red')

''' O usando reversed (reversed devuelve un iterable que se convierte en una tupla'''
colors = "red", "green", "blue"
rev = tuple(reversed(colors))
colors = rev
print(rev)
print(colors)       # ('blue', 'green', 'red')