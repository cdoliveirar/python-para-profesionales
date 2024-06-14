'''
Metaclases

Las metaclases te permiten modificar profundamente el comportamiento de las clases de Python (en términos de cómo se
definen, instancian, acceden, y más) al reemplazar la metaclase 'type' que las nuevas clases utilizan por defecto
'''

'''
Metaclases básicas
Cuando se llama a type con tres argumentos, se comporta como la (meta) clase que es y crea una nueva instancia, 
es decir, produce una nueva clase/tipo.
'''
Dummy = type('OtherDummy', (), dict(x=1))

print(Dummy.__class__)          # <class 'type'>
print(Dummy().__class__.__class__)  # <class 'type'>

''' Es posible heredar de type para crear una metaclase personalizada.'''
class mytype(type):
    def __init__(cls, name, bases, dict):
        # Llamar al inicializador base
        type.__init__(cls, name, bases, dict)
        # Realizar inicialización personalizada...
        cls.__custom_attribute__ = 2

''' Ahora, tenemos una nueva metaclase personalizada mytype que se puede usar para crear clases de la misma manera que 
type.'''

MyDummy = mytype('MyDummy', (), dict(x=2))

print(MyDummy.__class__)                # <class '__main__.mytype'>
print(MyDummy().__class__.__class__)    # <class '__main__.mytype'>
print(MyDummy.__custom_attribute__)     # 2

''' Cuando creamos una nueva clase utilizando la palabra clave class, la metaclase se elige por defecto en función de 
las clases base.'''

class Foo(object):
    pass


print(type(Foo))        # <class 'type'>

''' En el ejemplo anterior, la única clase base es object, por lo que nuestra metaclase será el tipo de object, que es 
type. Es posible sobrescribir el valor predeterminado usando un argumento de palabra clave especial metaclass 
para especificar la metaclase.'''

class MyDummy(metaclass=mytype):
    pass

print(type(MyDummy))        #   <class '__main__.mytype'>


''' Cualquier argumento de palabra clave (excepto metaclass) en la declaración de clase se pasará a la metaclase. Por 
lo tanto, class MyDummy(metaclass=mytype, x=2) pasará x=2 como argumento de palabra clave al constructor de mytype.

https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python/6581949#6581949

'''



