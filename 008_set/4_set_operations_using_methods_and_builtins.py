'''

'''
from enum import Enum


def function_set_operations_using_methods_and_builtins():
    # We deﬁne two sets a and b
    a = {1, 2, 2, 3, 4}
    b = {3, 3, 4, 4, 5}

    # Intersection
    # a.intersection(b) returns a new set with elements present in both a and b
    print(  a.intersection(b)  )            # {3, 4}

    # Union
    # a.union(b) returns a new set with elements present in either a and b
    print(  a.union(b)      )               # {1, 2, 3, 4, 5}

    # Diﬀerence
    # a.difference(b) returns a new set with elements present in a but not in b
    print(  a.difference(b)     )           # {1, 2}
    print(  b.difference(a)     )           # {5}

    # Symmetric Diﬀerence
    # a.symmetric_difference(b) returns a new set with elements present in either a or b but not in both
    print(  a.symmetric_difference(b)       )   #   {1, 2, 5}
    print(  b.symmetric_difference(a)       )   #   {1, 2, 5}


    # NOTE: a.symmetric_difference(b) == b.symmetric_difference(a)

    # Subset and superset
    # c.issubset(a) tests whether each element of c is in a .
    # a.issuperset(c) tests whether each element of c is in a .
    c = {1, 2}
    print(  c.issubset(a)    )              # True
    print(  a.issuperset(c)  )              # True


    # Disjoint sets
    # Sets a and d are disjoint if no element in a is also in d and vice versa.
    d = {5, 6}
    print(  a.isdisjoint(b)    )            # False
    print(  a.isdisjoint(d)    )            # True

    # This is an equivalent check, but less efficient
    print(  len(a & d) == 0   )             # True

    # This is even less efficient
    print(  a & d == set()    )             # True

    # Testing membership
    # The builtin in keyword searches for occurances
    print(  1 in a)                         # True
    print(  6 in a)                         # False

    # Length
    # The builtin len() function returns the number of elements in the set
    print(  len(a)    )                     # 4
    print(  len(b)    )                     # 3




if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_set_operations_using_methods_and_builtins()