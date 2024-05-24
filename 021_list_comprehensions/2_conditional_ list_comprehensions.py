'''
Dada una list comprehension, puedes añadir una o más condiciones if para filtrar valores.

[<expression> for <element> in <iterable> if <condition>]

Para cada <element> en <iterable>; si <condition> se evalúa como True, añade <expression> (usualmente una función
de <element>) a la lista devuelta.
'''

''' Por ejemplo, esto se puede usar para extraer solo los números pares de una secuencia de enteros'''

print([x for x in range(10) if x % 2 == 0])     # [0, 2, 4, 6, 8]

# El codigo de arriba es equivalente a :
even_numbers = []
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)

'''
Además, una list comprehension condicional de la forma [e for x in y if c] (donde e y c son expresiones en términos 
de x) es equivalente a list(filter(lambda x: c, map(lambda x: e, y))).
'''

''' A pesar de proporcionar el mismo resultado, ten en cuenta que el primer ejemplo es casi dos veces más rápido 
que el segundo. Para aquellos que tienen curiosidad, esta es una buena explicación del por qué.'''

''' Nota que esto es bastante diferente de la expresión condicional ... if ... else ... (a veces conocida como una 
expresión ternaria) que puedes usar para la parte <expression> de la list comprehension. Considera el siguiente 
ejemplo:'''

print([x if x % 2 == 0 else None for x in range(10)])       # [0, None, 2, None, 4, None, 6, None, 8, None]

''' Aquí la expresión condicional no es un filtro, sino un operador que determina el valor que se usará para los 
elementos de la lista:

<value-if-condition-is-true> if <condition> else <value-if-condition-is-false>

Esto se vuelve más obvio si lo combinas con otros operadores:
'''

print([2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)])
# [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

# El codigo de arriba es equivalente a:
numbers = []
for x in range(10):
    if x % 2 == 0:
        temp = x
    else:
        temp = -1
    numbers.append(2 * temp + 1)
print(numbers)      # [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

''' Se pueden combinar expresiones ternarias y condiciones if. El operador ternario funciona sobre el resultado 
filtrado'''
print([x if x > 2 else '*' for x in range(10) if x % 2 == 0])
# ['*', '*', 4, 6, 8]

''' Lo mismo no podría haberse logrado solo con el operador ternario '''
print([x if (x > 2 and x % 2 == 0) else '*' for x in range(10)])
# ['*', '*', '*', '*', 4, '*', 6, '*', 8, '*']


