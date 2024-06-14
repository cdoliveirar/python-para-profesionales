'''
Herencia Multiple
'''

''' Python utiliza el algoritmo de linealización C3 para determinar el orden en el que se resuelven los atributos de 
clase, incluidos los métodos. Esto se conoce como el Orden de Resolución de Métodos (MRO, por sus siglas en inglés).'''

# https://en.wikipedia.org/wiki/C3_linearization

class Foo(object):
    foo = 'attr foo of Foo'

class Bar(object):
    foo = 'attr foo of Bar'  # no veremos esto.
    bar = 'attr bar of Bar'

class FooBar(Foo, Bar):
    foobar = 'attr foobar of FooBar'

''' Ahora, si instanciamos FooBar, al buscar el atributo foo, vemos que primero se encuentra el atributo de Foo:'''
fb = FooBar()

print(fb.foo)           # attr foo of Foo

# Aquí está el MRO de FooBar:

print(FooBar.mro())     # [<class '__main__.FooBar'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <class 'object'>]

''' Puede decirse simplemente que el algoritmo MRO (Method Resolution Order) de Python es:

1- Primero en profundidad (por ejemplo, FooBar luego Foo) a menos que
2- un padre compartido (object) sea bloqueado por un hijo (Bar) y
3- no se permiten relaciones circulares.


Es decir, por ejemplo, Bar no puede heredar de FooBar mientras FooBar hereda de Bar.

Para un ejemplo comprensivo en Python, podrias visitar https://en.wikipedia.org/wiki/C3_linearization

Otra característica poderosa en la herencia es super.super puede obtener características de las clases padres.
'''

class Foo(object):
    def foo_method(self):
        print("foo Method")

class Bar(object):
    def bar_method(self):
        print("bar Method")

class FooBar(Foo, Bar):
    def foo_method(self):
        super(FooBar, self).foo_method()



''' La herencia múltiple con el método init de la clase, cuando cada clase tiene su propio método __init__, entonces 
intentamos para herencia múltiple, solo se llama al método init de la clase que se hereda primero. Por ejemplo:'''

class Foo(object):
    def __init__(self):
        print("foo init")

class Bar(object):
    def __init__(self):
        print("bar init")

class FooBar(Foo, Bar):
    def __init__(self):
        print("foobar init")
        super(FooBar, self).__init__()

a = FooBar()
print(a)
# foobar init
# foo init

''' Pero eso no significa que la clase Bar no se herede. La instancia de la clase final FooBar también es instancia de 
la clase Bar y de la clase Foo.
'''
print(isinstance(a, FooBar))    # True
print(isinstance(a, Foo))       # True
print(isinstance(a, Bar))       # True

