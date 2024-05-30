'''
Una tupla es una lista inmutable de valores. Las tuplas son uno de los tipos de colección más simples y comunes de
Python, y se pueden crear con el operador coma (valor = 1, 2, 3)."
'''

''' Sintácticamente, una tupla es una lista de valores separados por comas:'''
t = 'a', 'b', 'c', 'd', 'e'
print(type(t))


''' Aunque no es necesario, es común encerrar las tuplas entre paréntesis'''
t = ('a', 'b', 'c', 'd', 'e')
print(type(t))          # <class 'tuple'>

''' Crear una tupla vacia con parentesis'''
t0 = ()
print(type(t0))         # <class 'tuple'>

''' Para crear una tupla con un solo elemento, debes incluir una coma final'''
t1 = 'a',
print(type(t1))         # <class 'tuple'>

'''Ten en cuenta que un solo valor entre paréntesis no es una tupla '''
t2 = ('a')
print(type(t2))         # <class 'str'>

''' Para crear una tupla de un solo elemento es necesario incluir una coma al final.'''
t2 = ('a',)
print(type(t2))         # <class 'tuple'>

t2 = ('a',)             # EP8-compliant
t2 = 'a',               # esta notación no es recomendada por PEP8
t2 = ('a', )            # esta notación no es recomendada por PEP8


''' Otra manera de crear una tupla es mediante la función integrada tuple.'''
t = tuple('lupins')         # ('l', 'u', 'p', 'i', 'n', 's')
print(t)
t = tuple(range(3))         # (0, 1, 2)
print(t)

''' Si deseas crear una tupla con un solo elemento que sea el string completo, debes encerrar el string entre 
paréntesis:'''
mi_tupla = ('lupins',)  # Nota la coma al final
print(mi_tupla)         # ('lupins',)
