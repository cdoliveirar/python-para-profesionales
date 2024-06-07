'''
Extraer valores uno por uno
'''

''' Empieza con iter() integrado para obtener un iterador sobre el iterable y usa next() para obtener los elementos 
uno por uno hasta que se genere StopIteration, lo que indica el final.'''

s = {1, 2}		# lista o generador o incluso iterador
i = iter(s)		# obtener el iterator
a = next(i)		# a = 1
b = next(i)		# b = 2
c = next(i)		# raises StopIteration

# una mejora para tratar excepcion

s = {1, 2}      # conjunto (que es iterable)
i = iter(s)     # obtener el iterador
a = next(i)     # a = 1
b = next(i)     # b = 2
try:
    c = next(i)     # raises StopIteration
except StopIteration:
    print("Se ha agotado el iterador")
