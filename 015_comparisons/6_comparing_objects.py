'''
Para comparar la igualdad de clases personalizadas, puedes sobrescribir == y != mediante la definición de los
métodos __eq__ y __ne__. También puedes sobrescribir __lt__ (<), __le__ (<=), __gt__ (>), y __ge__ (>=).
Ten en cuenta que solo necesitas sobrescribir dos métodos de comparación, y Python puede manejar el resto
(== es lo mismo que no < y no >, etc.).
'''

class Foo(object):
    def __init__(self, item):
        self.my_item = item
    def __eq__(self, other):
        return self.my_item == other.my_item

a = Foo(5)
b = Foo(5)
print(a == b)           # True
print(a != b)           # False
print(a is b)           # False

# Mismo tipo de objeto
'''
Ten en cuenta que esta comparación simple asume que el otro objeto (el objeto con el que se está comparando) 
es del mismo tipo de objeto. Comparar con otro tipo de objeto lanzará un error.
'''

class Bar(object):
    def __init__(self, item):
        self.other_item = item
    def __eq__(self, other):
        return self.other_item == other.other_item
    def __ne__(self, other):
        return self.other_item != other.other_item

c = Bar(5)
print(a == c)       #  AttributeError: 'Bar' object has no attribute 'my_item'

# Usar isinstance() o similar ayudará a prevenir esto (si se desea).

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


