'''
Clase decoradora
'''

'''
Como se mencionó en la introducción, un decorador es una función que puede aplicarse a otra función para aumentar su 
comportamiento. El azúcar sintáctica es equivalente a lo siguiente: my_func = decorator(my_func). Pero ¿qué pasaría si 
el decorador fuera en cambio una clase? La sintaxis seguiría funcionando, excepto que ahora my_func se reemplazaría 
con una instancia de la clase decoradora. Si esta clase implementa el método mágico call(), entonces seguiría siendo 
posible usar my_func como si fuera una función.
'''

class Decorator(object):
    """Simple clase deceradora """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function.')

print(testfunc())
# Before the function call.
# Inside the function.
# After the function call.
# None

''' Ten en cuenta que una función decorada con un decorador de clase ya no será considerada una "función" desde la 
perspectiva de la comprobación de tipos.'''

import types
print(isinstance(testfunc, types.FunctionType))     # False

print(type(testfunc))       # <class '__main__.Decorator'>

''' Decorando Métodos
Para decorar métodos, necesitas definir un método adicional __get__
'''

from types import MethodType
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Inside the decorator.')
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        # Devuelve un Método si se llama desde una instancia
        return self if instance is None else MethodType(self, instance)


class Test(object):
    @Decorator
    def __init__(self):
        pass

a = Test()      # Inside the decorator.

''' 
¡Advertencia!
Los decoradores de clases solo producen una instancia para una función específica, por lo que decorar un método con un 
decorador de clase compartirá el mismo decorador entre todas las instancias de esa clase.
'''
from types import MethodType


class CountCallsDecorator(object):
    def __init__(self, func):
        self.func = func
        self.ncalls = 0         # Numnero de llamadas de este medoto

    def __call__(self, *args, **kwargs):
        self.ncalls += 1       # contador de incremento de llamadas
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)


class Test1(object):
    def __init__(self):
        pass

    @CountCallsDecorator
    def do_something(self):
        return 'something was done'

a = Test1()
print(a.do_something())
print(a.do_something.ncalls)        # 1
b = Test1()
print(b.do_something())
print(b.do_something.ncalls)        # 2