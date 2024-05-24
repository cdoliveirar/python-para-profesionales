'''
Generator Expressions

Las expresiones generadoras son muy similares a las comprensiones de listas. La principal diferencia es que no crea un
conjunto completo de resultados de una vez; crea un objeto generador que luego se puede iterar
'''

# list comprehensions
print([x**2 for x in range(10)])        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# generator comprehension
print((x**2 for x in range(10)))        # <generator object <genexpr> at 0x7f2488ce3660>

''' Estos son dos objetos muy diferentes:
- La comprensión de lista devuelve un objeto de lista, mientras que la comprensión de generador devuelve un generador.
- Los objetos generador no pueden ser indexados y hacen uso de la función next para obtener elementos en 
orden(solo python2)
'''

for i in [x**2 for x in range(10)]:
    print(i)

'''  Casos de uso  

Las expresiones generadoras son evaluadas de forma perezosa, lo que significa que generan y devuelven cada valor 
solo cuando el generador es iterado. Esto es frecuentemente útil al iterar a través de conjuntos de datos grandes, 
evitando la necesidad de crear una duplicación del conjunto de datos en la memoria:

for square in (x**2 for x in range(1000000)):
    #do something
'''

'''
Otro caso de uso común es evitar iterar sobre un iterable completo si no es necesario. En este ejemplo, se recupera un 
elemento de una API remota con cada iteración de get_objects(). Pueden existir miles de objetos, deben ser recuperados 
uno por uno, y solo necesitamos saber si existe un objeto que coincida con un patrón. Al usar una expresión generadora, 
cuando encontramos un objeto que coincide con el patró


def get_objects():
"""Gets objects from an API one by one"""
    while True:
        yield get_next_item()

def object_matches_pattern(obj):
    # perform potentially complex calculation
    return matches_pattern

def right_item_exists():
    items = (object_matched_pattern(each) for each in get_objects())
    for item in items:
        if item.is_the_right_one:
            return True
    return  False

'''