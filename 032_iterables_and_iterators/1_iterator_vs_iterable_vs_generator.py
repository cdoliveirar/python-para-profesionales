'''
Iterator vs Iterable vs Generator
'''

'''
Un iterable es un objeto que puede devolver un iterador. Cualquier objeto con estado que tenga un método __iter__ y 
devuelva un iterador es un iterable. También puede ser un objeto sin estado que implemente un método __getitem__. - 
El método puede tomar índices (empezando desde cero) y generar un IndexError cuando los índices ya no son válidos. 

La clase str de Python es un ejemplo de un iterable __getitem__. 

Un iterador es un objeto que produce el próximo valor en una secuencia cuando llamas a next(*objeto*) en algún objeto. 
Además, cualquier objeto con un método __next__ es un iterador. Un iterador genera un StopIteration después de agotar 
el iterador y no puede ser reutilizado en este punto.
'''

''' Iterable classes
Las clases iterables definen un método __iter__ y un método __next__. Ejemplo de una clase iterable
'''
class MyIterable:
    def __iter__(self):
        return self
    def __next__(self):
        pass #code

# En versiones más antiguas de Python, todavía se admite el objeto iterable clásico, __getitem__...
class MySequence:
    def __getitem__(self, index):
        if (condition):
            raise IndexError
        return (item)

ex2 = MySequence()
for (item) in (ex2):
    pass    #code