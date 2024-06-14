'''
Usando una metaclases

class MyClass(metaclass=SomeMetaclass):
    pass
'''


# Dificiento la metaclase type
''' En Python, todo es un objeto, incluyendo las clases. Una metaclase es la clase de una clase. Es decir, una metaclase 
define el comportamiento de las clases, así como una clase normal define el comportamiento de los objetos.
La metaclase predeterminada en Python es type. Cuando se define una clase, Python crea automáticamente un objeto de la 
clase type para representar esa clase.
Por ejemplo, cuando escribes:'''

class MiClase:
    pass

''' Python internamente crea un objeto type llamado MiClase. Este objeto type es una instancia de type misma, que es 
la metaclase.
comprueba:'''

class MiClase:
    pass

print(MiClase.__class__)        # <class 'type'>

print(type(MiClase))            # <class 'type'>
