'''
Clase Singleton
'''

''' 
Clase Singleton

Un singleton es un patrón que restringe la instanciación de una clase a una sola instancia/objeto. Para obtener más 
información sobre los patrones de diseño de singleton en Python, consulta aquí.

https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

'''

class Singleton:
    def __new__(cls):
        try:
            it = cls.__it__
        except AttributeError:
            it = cls.__it__ = object.__new__(cls)
        return it

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__.upper())

    def __eq__(self, other):
        return other is self


''' Otro método es decorar tu clase. Siguiendo el ejemplo de esta respuesta, crea una clase Singleton:'''

class Singleton:
    """
    Una clase auxiliar no segura para subprocesos para facilitar la implementación de singletons.
    Esto debería usarse como un decorador, no como una metaclase, para la
    clase que debería ser un singleton.
    La clase decorada puede definir una función `__init__` que
    solo toma el argumento `self`. Aparte de eso, no hay
    restricciones que se apliquen a la clase decorada.
    Para obtener la instancia singleton, usa el método `Instance`. Intentar
    usar `__call__` resultará en que se genere un `TypeError`.
    Limitaciones: La clase decorada no puede ser heredada.
    """
    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Devuelve la instancia singleton. En su primera llamada, crea una
        nueva instancia de la clase decorada y llama a su método `__init__`.
        En todas las llamadas siguientes, se devuelve la instancia ya creada.
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Los singletons deben accederse a través de `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


''' Para usarlo, puedes usar el método Instance:'''
@Singleton
class Single:
    def __init__(self):
        self.name = None
        self.val = 0

    def getName(self):
        print(self.name)

x = Single.Instance()
y = Single.Instance()

x.name = 'Soy solteros'
x.getName()         #  Soy soltero
y.getName()         #  Soy soltero
