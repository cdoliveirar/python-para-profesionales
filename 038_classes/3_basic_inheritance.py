'''
Herencia básica
'''

''' La herencia en Python se basa en ideas similares a las utilizadas en otros lenguajes orientados a objetos como Java, 
C++, etc. Una nueva clase puede derivarse de una clase existente de la siguiente manera.'''

class BaseClass(object):
    pass


class DerivedClass(BaseClass):
    pass


''' La BaseClass es la clase ya existente (padre) y la DerivedClass es la nueva clase (hija) que hereda (o subclasifica)
 atributos de BaseClass. todas las clases heredan implícitamente de la clase object, que es la clase base para todos 
 los tipos incorporados.'''

''' Definimos una clase padre Rectangle en el ejemplo a continuación, que hereda implícitamente de object.'''


class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


''' La clase Rectangle se puede usar como clase base para definir una clase Square, ya que un cuadrado es un caso 
especial de rectángulo.'''

class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super(Square, self).__init__(s, s)
        self.s = s

''' La clase Square heredará automáticamente todos los atributos de la clase Rectangle, así como de la clase object. 
super() se utiliza para llamar al método __init__() de la clase Rectangle, llamando esencialmente a cualquier método 
sobrescrito de la clase base. Nota: en Python 3, super() no requiere argumentos. Los objetos de la clase derivada 
pueden acceder y modificar los atributos de sus clases base'''

''' Los objetos de la clase derivada pueden acceder y modificar los atributos de sus clases base'''

r = Rectangle(3,4)
print(r.area())             # 12
print(r.perimeter())        # 14

s = Square(2)
print(s.area())             # 12
print(s.perimeter())        # 8

''' Funciones incorporadas que funcionan con la herencia  (Built-in functions)

issubclass(DerivedClass, BaseClass): devuelve True si DerivedClass es una subclase de BaseClass.

isinstance(s, Class): devuelve True si s es una instancia de Class o de cualquiera de las clases derivadas de Class.
'''

# subclass check
print(issubclass(Square, Rectangle))        # True

# Instanciar
r = Rectangle(3, 4)
s = Square(2)

print(isinstance(r, Rectangle))     # True
print(isinstance(r, Square))        # False, Un rectangulo no es un Cuadrado.

print(isinstance(s, Rectangle))     # True, Un cuadrado es un Rectangulo
print(isinstance(s, Square))        # True

