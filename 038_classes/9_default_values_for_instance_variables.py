'''
Valores predeterminados para variables de instancia
'''

''' Si la variable contiene un valor de un tipo inmutable (por ejemplo, una cadena), entonces está bien asignar un 
valor predeterminado de esta manera'''

class Rectangle(object):
    def __init__(self, width, height, color='blue'):
        self.width = width
        self.height = height
        self.color = color

    def area(self):
        return self.width * self.height

# Crear algunas instancias de la clase
default_rectangle = Rectangle(2, 3)
print(default_rectangle.color)  # blue
red_rectangle = Rectangle(2, 3, 'red')
print(red_rectangle.color)  # red


''' Uno debe tener cuidado al inicializar objetos mutables, como listas, en el constructor. Considera el siguiente 
ejemplo:'''
class Rectangle2D(object):
    def __init__(self, width, height, pos=[0,0], color='blue'):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color

r1 = Rectangle2D(5, 3)
r2 = Rectangle2D(7, 8)
r1.pos[0] = 4
print(r1.pos)       # [4, 0]
print(r2.pos)       # [4, 0] el `pos` de `r2` también ha cambiado

''' Este comportamiento se debe al hecho de que en Python los parámetros predeterminados se enlazan en la declaración 
de la función y no en la ejecución de la función.. Para obtener una variable de instancia predeterminada que no se 
comparta entre instancias, se debe usar una construcción como esta'''

class Rectangle2D(object):
    def __init__(self, width, height, pos=None, color='blue'):
        self.width = width
        self.height = height
        self.pos = pos or [0, 0]        # el valor predeterminado es [0, 0]
        self.color = color

r1 = Rectangle2D(5, 3)
r2 = Rectangle2D(7, 8)
r1.pos[0] = 4
print(r1.pos)           # [4, 0]
print(r2.pos)           # [0, 0] el `pos` de `r2` no ha cambiado




