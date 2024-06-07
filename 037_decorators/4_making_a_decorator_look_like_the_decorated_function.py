'''
Hacer que un decorador se parezca a la función decorada
'''

''' Los decoradores normalmente eliminan los metadatos de la función ya que no son iguales. Esto puede causar problemas 
al utilizar la meta-programación para acceder dinámicamente a los metadatos de la función. Los metadatos también 
incluyen la cadena de documentación de la función y su nombre. functools.wraps hace que la función decorada se parezca 
a la función original copiando varios atributos a la función envoltorio.'''

from functools import wraps

''' Los dos métodos de envolver un decorador logran lo mismo al ocultar que la función original ha sido decorada. 
No hay razón para preferir la versión de función a la versión de clase a menos que ya estés usando una sobre la 
otra.'''

''' As a function '''
def decorator(func):
# Copia el docstring, name, annotations y module a el  decorator
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped_func

@decorator
def test():
    pass

print(test.__name__)        # test


''' Como una clase '''
class Decorator(object):
    def __init__(self, func):
        # Copia name, module, annotations y docstring a la instancia.
        self._wrapped = wraps(func)(self)
    def __call__(self, *args, **kwargs):
        return self._wrapped(*args, **kwargs)

@Decorator
def test1():
    """Docstring of test."""
    pass

print(test1.__doc__)        # Docstring of test.
