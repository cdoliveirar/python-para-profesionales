'''
Propiedades
'''

''' Las clases de Python admiten propiedades, que se parecen a variables de objeto regulares, pero con la posibilidad 
de adjuntar comportamiento personalizado y documentación.'''

class MyClass(object):
    def __init__(self):
        self._my_string = ""

    @property
    def string(self):
        """Una cadena profundamente importante."""
        return self._my_string

    @string.setter
    def string(self, new_value):
        assert isinstance(new_value, str), \
            "¡Dame una cadena, no un %r!" % type(new_value)
        self._my_string = new_value

    @string.deleter
    def x(self):
        self._my_string = None


'''Los objetos de la clase MyClass parecerán tener una propiedad .string, sin embargo, su comportamiento está ahora 
estrechamente controlado '''

mc = MyClass()
mc.string = "¡Cadena!"
print(mc.string)
# del mc.string


''' Además de la útil sintaxis como se muestra arriba, la sintaxis de propiedad permite agregar validación u otras
mejoras a esos atributos. Esto podría ser especialmente útil con APIs públicas, donde se debe dar un nivel de ayuda al 
usuario.'''

''' Otro uso común de las propiedades es habilitar que la clase presente 'atributos virtuales' - atributos que no 
están realmente almacenados pero que se calculan solo cuando se solicitan.'''

class Character(object):
    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp

    # Hacer hp de solo lectura al no proporcionar un método set
    @property
    def hp(self):
        return self._hp

    # Hacer name de solo lectura al no proporcionar un método set
    @property
    def name(self):
        return self._name

    def take_damage(self, damage):
        self._hp -= damage
        self._hp = 0 if self._hp < 0 else self._hp

    @property
    def is_alive(self):
        return self._hp != 0

    @property
    def is_wounded(self):
        return self._hp < self._max_hp if self._hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive


bilbo = Character('Bilbo Baggins', 100)
print(bilbo.hp)         # 100

#bilbo.hp = 200          # AttributeError: can't set attribute
# el atributo hp es de solo lectura.

print(bilbo.is_alive)       # True

print(bilbo.is_wounded)     # False

print(bilbo.is_dead)        # False

bilbo.take_damage(50)

print(bilbo.hp)             # 50

print(bilbo.is_alive)       # True

print(bilbo.is_wounded)     # True

print(bilbo.is_dead)        # False

bilbo.take_damage(50)

print(bilbo.hp)             # 0

print(bilbo.is_alive)       # False

print(bilbo.is_wounded)     # False

print(bilbo.is_dead)        # True

