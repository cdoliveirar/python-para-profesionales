'''
Los SETs son colecciones desordenadas de elementos distintos. Pero a veces queremos trabajar con
colecciones desordenadas de elementos que no son necesariamente distintos y realizan un seguimiento
de las multiplicidades de los elementos.
'''
from enum import Enum


def function_sets_versus_multisets():
    setA = {'a', 'b', 'b', 'c'}
    print(setA)                     # {'a', 'c', 'b'}

    # By saving the strings 'a' , 'b' , 'b' , 'c' into a set data structure we've lost the information
    # on the fact that 'b'     # occurs twice. Of course saving the elements to a list would retain this information
    listA = ['a', 'b', 'b', 'c']
    print(  listA    )              # ['a', 'b', 'b', 'c']

    from collections import Counter
    counterA = Counter(['a', 'b', 'b', 'c'])
    print(counterA)                                 # Counter({'b': 2, 'a': 1, 'c': 1})

    # Counter es un diccionario donde los elementos se almacenan como claves de diccionario y sus recuentos
    # se almacenan como valores del diccionario. Y como todos los diccionarios, es una colección desordenada.



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_sets_versus_multisets()