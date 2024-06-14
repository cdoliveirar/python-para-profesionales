'''
Python se presenta no solo como un lenguaje de scripting popular, sino que también soporta el paradigma de programación
orientada a objetos. Las clases describen datos y proporcionan métodos para manipular esos datos, todo ello englobado
bajo un único objeto. Además, las clases permiten la abstracción al separar los detalles concretos de implementación
de las representaciones abstractas de los datos.

El código que utiliza clases es generalmente más fácil de leer,entender y mantener.
'''

''' Una clase funciona como una plantilla que define las características básicas de un objeto en particular.'''
class Person(object):
    """A simple class."""                               # docstring
    species = "Homo Sapiens"                            # atributo de clase

    def __init__(self, name):                           # metodo especial
        """ Este es el inicializador.
        Es un método especial """
        self.name = name                                # atributo de instancia

    def __str__(self):                                  # metodo especial
        """Este método se ejecuta cuando Python
        intenta convertir el objeto a una cadena.
        Devuelve esta cadena al usar print(), etc.
        """
        return self.name

    def rename(self, renamed):                          # metodo regular
        """Reasigna e imprime el atributo nombre."""
        self.name = renamed
        print("Now my name is {}".format(self.name))


''' Hay algunas cosas a tener en cuenta al mirar el ejemplo anterior
1. La clase se compone de atributos (datos) y métodos (funciones).

2. Los atributos y métodos se definen simplemente como variables y funciones normales.

3. Como se señala en la correspondiente cadena de documentación, el método init() se llama el inicializador. 
Es equivalente al constructor en otros lenguajes orientados a objetos, y es el método que se ejecuta primero cuando 
creas un nuevo objeto o una nueva instancia de la clase.

4. Los atributos que se aplican a toda la clase se definen primero y se llaman atributos de clase.

5. Los atributos que se aplican a una instancia específica de una clase (un objeto) se llaman atributos de instancia. 
Generalmente se definen dentro de __init__(); no es necesario, pero se recomienda (ya que los atributos definidos fuera 
de __init()__ corren el riesgo de ser accedidos antes de que sean definidos).

6. Cada método, incluido en la definición de la clase, pasa el objeto en cuestión como su primer parámetro. La palabra 
self se usa para este parámetro (el uso de self es en realidad por convención, ya que la palabra self no tiene un 
significado inherente en Python, pero esta es una de las convenciones más respetadas de Python, y siempre debes 
seguirla).

7. Aquellos acostumbrados a la programación orientada a objetos en otros lenguajes pueden sorprenderse por algunas 
cosas. Una de ellas es que Python no tiene un verdadero concepto de elementos privados, por lo que todo, por defecto, 
imita el comportamiento de la palabra clave public en C++/Java. 

8. Algunos de los métodos de la clase tienen la siguiente forma: nombre_función(self, otro_stuff). Todos estos métodos 
se llaman "métodos mágicos" y son una parte importante de las clases en Python. Por ejemplo, la sobrecarga de 
operadores en Python se implementa con métodos mágicos. 
'''

''' ¡Ahora hagamos unas cuantas instancias de nuestra clase Persona!'''

kelly = Person("Kelly")
joseph = Person("Joseph")
john_doe = Person("John Doe")

''' Actualmente tenemos tres objetos Persona, kelly, joseph y john_doe. Podemos acceder a los atributos de la clase 
desde cada instancia utilizando el operador punto. Nótese nuevamente la diferencia entre los atributos de clase y los 
de instancia.'''

print(kelly.species)        # Homo Sapiens
print(joseph.species)       # Homo Sapiens
print(john_doe.species)     # Homo Sapiens

print(kelly.name)           # Kelly
print(joseph.name)          # Joseph

''' Podemos ejecutar los métodos de la clase utilizando el mismo operador punto.'''
# Llamar explícitamente a __str__()
print(john_doe.__str__())   # John Doe
# Usar print, que llama implícitamente a __str__()
print(john_doe)
john_doe.rename("CArlos")
print(john_doe)