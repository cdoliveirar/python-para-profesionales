'''
Comprobando si un elemento está en una lista

Python hace que sea muy simple comprobar si un elemento está en una lista. Simplemente usa el operador in.
'''

lst = ['test', 'twest', 'tweast', 'treast']

print('test' in lst)        # True
print('toast' in lst)       # False

''' Nota: el operador in en conjuntos es asintóticamente más rápido que en listas. Si necesitas usarlo muchas veces en
listas potencialmente grandes, puede que desees convertir tu lista a set y probar la presencia de elementos 
en el set. '''

# Ahora usando set

slst = set(lst)
print('test' in slst)       # True