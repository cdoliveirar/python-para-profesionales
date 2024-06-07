'''
Funcoin Reduce
'''

''' Reduce toma una función y una colección de elementos. Devuelve un valor que se crea combinando los elementos. 
Este es un reduce simple. Devuelve la suma de todos los elementos de la colección.'''
from functools import reduce

total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total)

'''  
- Inicialmente, a es el primer elemento de la lista (0) y x es el segundo elemento (1). La función lambda se evalúa 
como 0 + 1, que resulta en 1.
- En la siguiente iteración, a es ahora 1 (el resultado de la iteración anterior) y x es el siguiente elemento de la 
lista (2). La función lambda se evalúa como 1 + 2, que resulta en 3.
- En la siguiente iteración, a es 3 y x es 3. La función lambda se evalúa como 3 + 3, que resulta en 6.
- En la última iteración, a es 6 y x es 4. La función lambda se evalúa como 6 + 4, que resulta en 10.

Finalmente, reduce devuelve el valor acumulado, que es 10, y se asigna a la variable total.
'''