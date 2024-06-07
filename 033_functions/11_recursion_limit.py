'''
Límite de recursión
'''

''' Existe un límite para la profundidad de la recursión posible, el cual depende de la implementación de Python. 
Cuando se alcanza el límite, se genera una excepción RuntimeError.'''

def cursing(depth):
    try:
        cursing(depth + 1) # actually, re-cursing
    except RuntimeError as RE:
        print('I recursed {} times!'.format(depth))

print(cursing(0))

''' Es posible cambiar el límite de profundidad de la recursión usando sys.setrecursionlimit(limit) y verificar este 
límite usando sys.getrecursionlimit().'''
import sys
sys.setrecursionlimit(2000)
cursing(0)

''' pero evitará que se genere una excepción RuntimeError debido a la profundidad máxima de recursión alcanzada.'''