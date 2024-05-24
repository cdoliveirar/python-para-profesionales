'''
Las funciones filter o map a menudo deberían ser reemplazadas por comprensiones de listas.
'''

'''
filter(P, S) casi siempre se escribe de manera más clara como [x for x in S if P(x)], y esto tiene la gran ventaja 
de que los usos más comunes implican predicados que son comparaciones, por ejemplo, x==42, y definir una lambda para 
eso requiere mucho más esfuerzo para el lector (además de que la lambda es más lenta que la comprensión de listas). 
Aún más para map(F, S) que se convierte en [F(x) for x in S]. Por supuesto, en muchos casos podrías usar expresiones 
generadoras en su lugar.
'''

'''
Las siguientes líneas de código se consideran "no pythonicas" y generarán errores en muchos linters de Python.
'''
from functools import reduce
print(filter(lambda x: x % 2 == 0, range(10))) # even numbers < 10
print(map(lambda x: 2*x, range(10))) # multiply each number by two
print(reduce(lambda x,y: x+y, range(10))) # sum of all elements in list

''' Tomando lo que hemos aprendido de la cita anterior, podemos descomponer estas expresiones de filter y map en sus 
comprensiones de lista equivalentes; también eliminando las funciones lambda de cada una, lo que hace que el código 
sea más legible en el proceso.
'''

# Filter:
# P(x) = x % 2 == 0
# S = range(10)
[x for x in range(10) if x % 2 == 0]

# Map
# F(x) = 2*x
# S = range(10)
[2*x for x in range(10)]

''' La legibilidad se hace aún más evidente al tratar con la encadenación de funciones. Donde, debido a la legibilidad, 
los resultados de una función map o filter deberían ser pasados como resultado al siguiente; en casos simples, 
estos pueden ser reemplazados con una sola comprensión de lista. Además, podemos determinar fácilmente a partir de la 
comprensión de lista cuál es el resultado de nuestro proceso, donde hay una carga cognitiva mayor al razonar sobre el 
proceso encadenado de Map & Filter.'''

# Map & Filter
filtered = filter(lambda x: x % 2 == 0, range(10))
results = map(lambda x: 2*x, filtered)
print(list(results))        # [0, 4, 8, 12, 16]

# List comprehension
results = [2*x for x in range(10) if x % 2 == 0]
print(results)              # [0, 4, 8, 12, 16]


'''
Refactorización - Referencia rápida'''
# Mapa
map(F, S) == [F(x) for x in S]
# Filter
filter(P, S) == [x for x in S if P(x)]

'''donde F y P son funciones que respectivamente transforman valores de entrada y devuelven un valor booleano.
'''

