'''
Singletons usando metaclases
'''

''' Un singleton es un patrón que restringe la instanciación de una clase a una única instancia/objeto '''

class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance

class MySingleton(metaclass=SingletonType):
    pass

print(MySingleton() is MySingleton())   # True, solo ocurre una instanciación

''' Esta implementación asegura que solo se crea una instancia de MySingleton, cumpliendo con el patrón singleton.'''

''' El operador is verifica que ambas llamadas devuelven exactamente la misma instancia, resultando en True.

Por lo tanto, MySingleton() is MySingleton() evalúa True porque SingletonType asegura que MySingleton siga el patrón 
singleton, permitiendo solo una instancia de la clase.
'''


