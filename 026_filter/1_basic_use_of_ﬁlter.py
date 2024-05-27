'''
Filtrar descarta elementos de una secuencia basado en algún criterio

La función filter se utiliza para construir un iterador a partir de aquellos elementos de un iterable
(como una lista, tupla, etc.) para los cuales una función dada devuelve True.

filter(function, iterable)
- function: Una función que toma un solo argumento y devuelve True o False.
- iterable: Una secuencia (como una lista, tupla, conjunto, etc.) cuyos elementos se filtrarán.

'''

names = ['Fred', 'Wilma', 'Barney']

def long_name(name):
    return len(name) > 5


print(list(filter(long_name, names)))                   # ['Barney'], Se usa filter para aplicar long_name a cada elemento
                                                        # de la lista names, y.casteo para lista

print([name for name in names if len(name) > 5])        # ['Barney']

print(tuple(name for name in names if len(name) > 5))   # ('Barney',) , casteo para tupla

