'''
Monkey Patching
'''

''' En este caso, "monkey patching" significa agregar una nueva variable o método a una clase después de que haya sido 
definida. Por ejemplo, supongamos que definimos la clase A como'''


class A(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return A(self.num + other.num)

''' Pero ahora queremos agregar otra función más adelante en el código. Supongamos que esta función es la siguiente:'''

def get_num(self):
    return self.num

''' Pero, ¿cómo agregamos esto como un método en A? Es simple, simplemente colocamos esa función en A con una 
declaración de asignación.'''

A.get_num = get_num

''' ¿Por qué funciona esto? Porque las funciones son objetos al igual que cualquier otro objeto, y los métodos son 
funciones que pertenecen a la clase.

La función get_num estará disponible para todas las instancias existentes (ya creadas) así como para las nuevas 
instancias de A. Estas adiciones están disponibles automáticamente en todas las instancias de esa clase (o sus 
subclases). Por ejemplo:'''

foo = A(42)
A.get_num = get_num

bar = A(6)
print(foo.get_num())            # 42
print(bar.get_num())            # 6


''' Nota que, a diferencia de algunos otros lenguajes, esta técnica no funciona para ciertos tipos incorporados, y no 
se considera una buena práctica.'''
