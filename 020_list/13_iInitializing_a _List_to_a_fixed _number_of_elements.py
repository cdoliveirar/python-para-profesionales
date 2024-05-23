'''
Inicializando una lista con un número fijo de elementos

Para elementos inmutables (por ejemplo, None, literales de cadena, etc.):
'''

my_list = [None] * 10
my_list = ['test'] * 10

print(my_list)


''' Para elementos mutables, el mismo constructo hará que todos los elementos de la lista se refieran al mismo objeto, 
por ejemplo, para un conjunto.'''

my_list=[{1}] * 10

print(my_list)

my_list[0].add(2)
print(my_list)


''' En cambio, para inicializar la lista con un número fijo de objetos mutables diferentes, us'''

my_list=[{1} for _ in range(10)]
print(my_list)

''' El guion bajo _ se usa cuando no necesitamos utilizar el valor que se genera en cada iteración del bucle, solo 
necesitamos el hecho de que se está repitiendo 10 veces'''