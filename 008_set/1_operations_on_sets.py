'''
Enums are iterable:
'''
from enum import Enum


def function_operations_on_sets():
    '''WITH OTHERS SETS'''

    # Intersection
    print(   {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})   )         # {3, 4, 5}
    print(   {1, 2, 3, 4, 5} & {3, 4, 5, 6}   )                     # {3, 4, 5}

    # Union
    print(  {1, 2, 3, 4, 5}.union({3, 4, 5, 6})  )                  # {1, 2, 3, 4, 5, 6}
    print(  {1, 2, 3, 4, 5} | {3, 4, 5, 6}  )                       # {1, 2, 3, 4, 5, 6}

    # Difference
    print(  {1, 2, 3, 4}.difference({2, 3, 5})   )                  # {1, 4}
    print(  {1, 2, 3, 4} - {2, 3, 5}    )                           # {1, 4}

    # Symmetric difference with)
    print(  {1, 2, 3, 4}.symmetric_difference({2, 3, 5}   ))        # {1, 4, 5}
    print(  {1, 2, 3, 4} ^ {2, 3, 5}    )                           # {1, 4, 5}

    # Superset check
    print(  {1, 2}.issuperset({1, 2, 3})       )                    # False
    print(  {1, 2} >= {1, 2, 3}     )                               # False

    # Disjoint check
    print(  {1, 2}.isdisjoint({3, 4})       )                       # True
    print(  {1, 2}.isdisjoint({1, 4})       )                       # False

    '''WITH SINGLE ELEMENTS'''
    # Existence check
    print(  2 in {1,2,3}        )                                   # True
    print(  4 in {1,2,3}        )                                   # False
    print(  4 not in {1,2,3}    )                                   # True

    s = {1, 2}
    s.update({3, 4})
    print(s)                                                       # {1, 2, 3, 4}





    # Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_operations_on_sets()