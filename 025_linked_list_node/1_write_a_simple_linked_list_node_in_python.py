'''
Una lista enlazada es:

- la lista vacía, representada por None, o
- un nodo que contiene un objeto de carga y una referencia a una lista enlazada.
'''

class Node:
    def __init__(self, cargo=None, next=None):
        self.car = cargo
        self.cdr = next

    def __str__(self):
        return str(self.car)
    def display(lst):
        if lst:
            print("%s " % lst)
            display(lst.cdr)
        else:
            print("nil\n")