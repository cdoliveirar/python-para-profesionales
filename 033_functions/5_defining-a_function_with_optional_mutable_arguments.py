'''
Definir una función con argumentos mutables opcionales
'''

''' Hay un problema al usar argumentos opcionales con un tipo predeterminado mutable (descrito en Definir una función 
con argumentos opcionales), lo que potencialmente puede llevar a un comportamiento inesperado.

Explicación

Este problema surge porque los argumentos predeterminados de una función se inicializan una vez, en el momento en que 
se define la función, y no (como en muchos otros lenguajes) cuando se llama a la función. Los valores predeterminados 
se almacenan dentro de la variable miembro defaults del objeto de función.

'''
def f(a, b=42, c=[]):
    pass
print(f.__defaults__)       # (42, [])

''' Para los tipos inmutables (ver Paso de argumentos e inmutabilidad) esto no es un problema porque no hay manera de 
mutar la variable; solo puede ser reasignada, dejando el valor original sin cambios. Por lo tanto, se garantiza que 
las llamadas subsiguientes tendrán el mismo valor predeterminado. Sin embargo, para un tipo mutable, el valor original 
puede mutar al hacer llamadas a sus diversas funciones miembro. Por lo tanto, no se garantiza que las llamadas 
sucesivas a la función tengan el valor predeterminado inicial.'''

def append(elem, to=[]):
    to.append(elem)         # Esta llamada a append() muta la variable predeterminada "to".
    return to

print(append(1))                # [1]
print(append(2))                # [1, 2]
print(append(2, []))    # [2]   , Usar una lista recién creada da el resultado esperado!!.
# Llamarlo de nuevo sin argumento añadirá a la lista almacenada internamente otra vez.
print(append(4))                # [1, 2, 4]

'''
Solución

Si deseas asegurarte de que el argumento predeterminado sea siempre el que especificas en la definición de la función, 
la solución es usar siempre un tipo inmutable como tu argumento predeterminado.

Un enfoque común para lograr esto cuando se necesita un tipo mutable como predeterminado es usar None (inmutable) como 
el argumento predeterminado y luego asignar el valor predeterminado real a la variable del argumento si es igual a None.
'''

def agregar_elemento(elem, to=None):
    if to is None:
        to = []
    to.append(elem)
    return to

print(agregar_elemento(1))                      # [1]
print(agregar_elemento(2))                      # [2]
print(agregar_elemento(3, [4, 5]))      # [4, 5, 3]
print(agregar_elemento(4))                      # [4]


''' Esto asegura que una nueva lista vacía se cree cada vez que la función se llame sin proporcionar un segundo 
argumento, evitando la mutación de la lista predeterminada entre llamadas a la función.'''
