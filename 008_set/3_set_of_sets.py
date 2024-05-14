'''
Digamos que tienes una lista de restaurantes; tal vez la leas de un archivo. Te importan los restaurantes únicos en
la lista. La mejor manera de obtener los elementos únicos de una lista es convertirla en un conjunto.
'''
from enum import Enum


def function_set_of_sets():

    # print( {{1, 2}, {3, 4}} )           # TypeError: unhashable type: 'set'

    # en ves usar frozenset

    print(  {frozenset({1, 2}), frozenset({3, 4})}      )



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_set_of_sets()