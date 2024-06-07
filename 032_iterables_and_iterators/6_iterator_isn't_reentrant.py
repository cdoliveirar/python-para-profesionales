'''
¡El iterador no es reentrante!
'''

def gen():
    yield 1
iterable = gen()
for a in iterable:
    print(a)

# ¿Cuál fue el primer elemento de iterable? No hay manera de obtenerlo ahora.
# Solo se puede obtener un nuevo iterador
gen()
