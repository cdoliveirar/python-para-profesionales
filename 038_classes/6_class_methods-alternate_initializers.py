'''
Métodos de clase: inicializadores alternativos
'''

''' Los métodos de clase presentan formas alternativas de crear instancias de clases. Para ilustrarlo, veamos un 
ejemplo. Supongamos que tenemos una clase Person relativamente simple:'''


class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")


''' Podría ser útil tener una forma de crear instancias de esta clase especificando un nombre completo en lugar de 
nombre y apellido por separado. Una forma de hacer esto sería tener last_name como un parámetro opcional, y asumir que 
si no se proporciona, se pasó el nombre completo:'''


class Person(object):
    def __init__(self, first_name, age, last_name=None):
        if last_name is None:
            self.first_name, self.last_name = first_name.split(" ", 2)
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.full_name = self.first_name + " " + self.last_name
            self.age = age
    def greet(self):
        print("Hello, my name is " + self.full_name + ".")

''' Sin embargo, hay dos problemas principales con este fragmento de código:

1- Los parámetros first_name y last_name ahora son engañosos, ya que puedes ingresar un nombre completo para first_name. 
Además, si hay más casos y/o más parámetros que tienen este tipo de flexibilidad, la ramificación con if/elif/else 
puede volverse molesta rápidamente.

2- No es tan importante, pero aún vale la pena mencionarlo: ¿qué pasa si last_name es None, pero first_name no se divide 
en dos o más partes mediante espacios? Tenemos otra capa más de validación de entrada y/o manejo de excepciones...

Aquí es donde entran los métodos de clase. En lugar de tener un único inicializador, crearemos un inicializador 
separado, llamado from_full_name, y lo decoraremos con el decorador (incorporado) classmethod.'''

class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name
    @classmethod
    def from_full_name(cls, name, age):
        if " " not in name:
            raise ValueError
        first_name, last_name = name.split(" ", 2)
        return cls(first_name, last_name, age)

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")


''' Observa cls en lugar de self como el primer argumento de from_full_name. Los métodos de clase se aplican a la clase 
en general, no a una instancia de una clase dada (que es lo que self usualmente denota). Entonces, si cls es nuestra 
clase Person, el valor devuelto del método de clase from_full_name es Person(first_name, last_name, age), que usa 
el __init__ de Person para crear una instancia de la clase Person. En particular, si hiciéramos una subclase Employee 
de Person, entonces from_full_name funcionaría también en la clase Employee.

Para mostrar que esto funciona como se espera, creemos instancias de Person de más de una manera sin la ramificación 
en __init__:'''

bob = Person("Bob", "Bobberson", 42)       # Se crea directamente usando el constructor __init__.
alice = Person.from_full_name("Alice Henderson", 31)        # Usando classmethod
# Se crea usando el método de clase from_full_name, que divide el nombre completo en nombre y apellido antes de llamar
# al constructor __init__.


print(bob.greet())
print(alice.greet())


''' 
Esto es útil para evitar la lógica condicional en __init__ y para mantener el código limpio y legible.

El código demuestra cómo usar métodos de clase para ofrecer múltiples formas de inicializar instancias de una clase, 
lo que puede ser particularmente útil cuando se trabaja con datos que vienen en diferentes formatos
'''
