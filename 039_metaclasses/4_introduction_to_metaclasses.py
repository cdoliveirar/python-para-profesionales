'''
Introducción a las Metaclases
'''

''' ¿Qué es una metaclase?
En Python, todo es un objeto: enteros, cadenas, listas, e incluso las funciones y las clases son objetos. Y cada objeto 
es una instancia de una clase. Para verificar la clase de un objeto x, se puede llamar a type(x)'''

print(type(5))              # <class 'int'>

print(type(str))            # <class 'type'>

print(type([1, 2, 3]))      # <class 'list'>

class C(object):
    pass

print(type(C))              # <class 'type'>


''' La mayoría de las clases en Python son instancias de type. type en sí mismo también es una clase. Estas clases 
cuyas instancias también son clases se llaman metaclases.'''

''' La metaclase más simple
Bien, ya existe una metaclase en Python: type. ¿Podemos crear otra?'''

class SimplestMetaclass(type):
    pass

class MyClass(object):
    __metaclass__ = SimplestMetaclass


''' Esto no añade ninguna funcionalidad, pero es una nueva metaclase. Observa que MyClass ahora es una instancia de 
SimplestMetaclass:
'''

print(type(MyClass))        # <class 'type'>


''' Una metaclase que hace algo'''
''' Una metaclase que hace algo usualmente sobrescribe el método __new__ de type para modificar algunas propiedades de 
la clase que se va a crear, antes de llamar al __new__ original que crea la clase:'''

class AnotherMetaclass(type):
    def __new__(cls, name, parents, dct):
        # cls es esta clase
        # name es el nombre de la clase que se va a crear
        # parents es la lista de las clases padres de la clase
        # dct es la lista de atributos de la clase (métodos, variables estáticas)
        # aquí se pueden modificar todos los atributos antes de crear la clase, por ejemplo:
        dct['x'] = 8
        # ahora la clase tendrá una variable estática x = 8
        # el valor de retorno es la nueva clase. super se encargará de eso
        return super(AnotherMetaclass, cls).__new__(cls, name, parents, dct)


