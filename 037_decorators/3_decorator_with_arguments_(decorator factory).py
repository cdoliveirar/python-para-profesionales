'''
Decorador con argumentos (factoría de decoradores)
'''

''' Un decorador toma solo un argumento: la función que se va a decorar. No hay forma de pasar otros argumentos.
Pero a menudo se desean argumentos adicionales. El truco entonces es hacer una función que tome argumentos arbitrarios 
y devuelva un decorador.'''


def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator

@decoratorfactory('Hola Mundo Decorador')
def test():
    pass

print(test())

''' Nota importante:
Con tales factories de decoradores, debes llamar al decorador con un par de paréntesis'''

@decoratorfactory # Without parentheses
def test():
    pass

#test()          # TypeError: decorator() missing 1 required positional argument: 'func'

''' Decorator classes '''
def decoratorfactory(*decorator_args, **decorator_kwargs):
    class Decorator(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
            print('Inside the decorator with arguments {}'.format(decorator_args))
            return self.func(*args, **kwargs)
    return Decorator


@decoratorfactory(10)
def test():
    pass

print(test())       # Inside the decorator with arguments (10,)

