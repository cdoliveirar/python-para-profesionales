'''
Concatenar y Fusionar listas

1.- La forma más simple de concatenar list1 y list2:
    merged = list1 + list2

2.- zip devuelve una lista de tuplas, donde la i-ésima tupla contiene el i-ésimo elemento de cada una de las secuencias
 o iterables de argumentos
'''


alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)
    # a1 b1
    # a2 b2
    # a3 b3

''' Si las listas tienen diferentes longitudes, entonces el resultado solo incluirá tantos elementos como la más 
corta.'''

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3', 'b4']
for a, b in zip(alist, blist):
    print(a, b)
    # a1 b1
    # a2 b2
    # a3 b3

alist = []
print(len(list(zip(alist, blist))))     # 0 , alist está vacía, por lo que no hay elementos para emparejar con blist.
                                        # Por lo tanto, la función zip() no produce ninguna tupla y la longitud
                                        # de la lista resultante es 0.

'''
Para rellenar listas de longitud desigual hasta la longitud de la más larga con valores None, use itertools.zip_longest 
(itertools.izip_longest en Python 2).
'''
import itertools

alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a,b,c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)
    # a1 b1 c1
    # a2 None c2
    # a3 None c3
    # None None c4

'''
Insertar valores en un índice específico
'''

alist = [123, 'xyz', 'zara', 'abc']
alist.insert(3, [2009])
print("Final List :", alist)        # Final List : [123, 'xyz', 'zara', [2009], 'abc']