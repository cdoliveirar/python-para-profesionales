'''
Variables de clase e instancia
'''

''' Las variables de instancia son únicas para cada instancia, mientras que las variables de clase son compartidas por 
todas las instancias.'''


class C:
    x = 2           # variable de clase

    def __init__(self, y):
        self.y = y          # variable de instancia

print(C.x)          # 2
# print(C.y)          # AttributeError: type object 'C' has no attribute 'y'

c1 = C(3)           # Se actualiza la instancia c2 con y=3
print(c1.x)         # 2

print(c1.y)         # 3


c2 = C(4)           # Se actualiza la instancia c2 con y=4
print(c2.x)         # 2

print(c2.y)         # 4

''' Las variables de clase se pueden acceder en instancias de esta clase, pero asignar a la variable de clase creará 
una variable de instancia que ocultará la variable de clase.'''

c2.x = 4
print(c2.x)     # 4
c1.x = 100
print(C.x)      # 2
print(c1.x)     # 100

''' Nota que modificar las variables de clase desde las instancias puede llevar a consecuencias inesperadas.'''

class D:
    x = []
    def __init__(self, item):
        self.x.append(item)  # nota que esto no es una asignación!

d1 = D(1)
d2 = D(2)
print(d1.x)     # [1, 2]
print(d2.x)     # [1, 2]
print(D.x)      # [1, 2]


''' esta variable de clase ha mitado para cada instancia'''

