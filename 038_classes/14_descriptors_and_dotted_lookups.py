'''
Descriptores y búsquedas punteadas
'''

''' Los descriptores son objetos que son (generalmente) atributos de clases y que tienen alguno de los métodos 
especiales __get__, __set__ o __delete__ .

Los Descriptores de Datos: tienen alguno de los métodos __set__ o __delete__ .

Estos pueden controlar la búsqueda punteada en una instancia y se utilizan para implementar funciones, staticmethod, 
classmethod y property. Una búsqueda punteada (por ejemplo, una instancia foo de la clase Foo buscando el atributo bar, 
es decir, foo.bar) utiliza el siguiente algoritmo:

1- Se busca bar en la clase, Foo. Si está allí y es un Descriptor de Datos, entonces se utiliza el descriptor de datos. 
Así es como property puede controlar el acceso a datos en una instancia y las instancias no pueden anular esto. Si no 
hay un Descriptor de Datos allí, entonces

2- Se busca bar en el __dict__ de la instancia. Es por eso que podemos anular o bloquear métodos que se llaman desde una 
instancia con una búsqueda punteada. Si bar existe en la instancia, se utiliza. Si no, entonces

3- Se busca en la clase Foo el bar. Si es un Descriptor, entonces se utiliza el protocolo de descriptor. Así es como se 
implementan funciones (en este contexto, métodos no ligados), classmethod y staticmethod. De lo contrario, simplemente 
devuelve el objeto allí, o si hay un AttributeError.
'''

''' 
Las "búsquedas punteadas" se refieren al acceso a atributos de un objeto mediante notación de punto, como en foo.bar, 
donde foo es una instancia de una clase y bar es un atributo o método de esa instancia o su clase.

Vamos a desglosar lo que significa todo el texto:

Descriptores
Los descriptores son objetos que controlan el acceso a los atributos de otras clases. Implementan uno o más de los 
siguientes métodos especiales:

__get__(self, instance, owner): para obtener un valor.
__set__(self, instance, value): para establecer un valor.
__delete__(self, instance): para eliminar un valor.


Descriptores de Datos
Estos son descriptores que implementan __set__ o __delete__, además de __get__. Los descriptores de datos tienen mayor
 precedencia en las búsquedas de atributos que los atributos de instancia.

Algoritmo de Búsqueda Punteada
Cuando se accede a un atributo de una instancia usando notación de punto (por ejemplo, foo.bar), Python sigue estos 
pasos:


1.- Buscar en la clase (Foo):

Si el atributo (bar) se encuentra en la clase (Foo) y es un Descriptor de Datos, se utiliza el descriptor de datos. 
Esto es como property puede controlar el acceso a los datos en una instancia. Las instancias no pueden anular esto.

2.- Buscar en el diccionario de la instancia (__dict__):

Si el atributo (bar) no es un descriptor de datos en la clase, Python busca en el diccionario de la instancia 
(foo.__dict__). Si bar está en __dict__, se utiliza este valor. Esto permite que los métodos sean anulados o 
bloqueados desde una instancia.

3.- Buscar en la clase de nuevo (Foo):

Si el atributo (bar) no se encuentra en el diccionario de la instancia, Python busca en la clase (Foo) nuevamente. 
Si bar es un Descriptor (pero no un descriptor de datos), se utiliza el protocolo de descriptor. Así es como se 
implementan classmethod, staticmethod y funciones (métodos no ligados en este contexto). Si bar no es un descriptor, 
simplemente devuelve el objeto encontrado en la clase. Si bar no se encuentra en la clase, se lanza un AttributeError.

Ejemplo
'''


class Descriptor:
    def __get__(self, instance, owner):
        return "Descriptor __get__"

class MyClass:
    attribute = Descriptor()

obj = MyClass()
print(obj.attribute)  # Descriptor __get__

'''
En este ejemplo, cuando accedemos a obj.attribute, Python sigue el algoritmo de búsqueda punteada:

1.- Busca attribute en la clase MyClass.
2.- Encuentra attribute y ve que es un descriptor (implementa __get__).
3.- Llama al método __get__ del descriptor, que devuelve "Descriptor __get__".
'''