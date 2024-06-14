'''
Métodos vinculados, no vinculados y estáticos
'''

''' La idea de los métodos vinculados y no vinculados fue eliminada en Python 3. En Python 3, cuando declaras un método 
dentro de una clase, utilizas la palabra clave def, creando así un objeto función. Esta es una función regular, y la 
clase que la rodea funciona como su espacio de nombres. En el siguiente ejemplo, declaramos el método f dentro de la 
clase A, y se convierte en una función A.f:'''

class A(object):
    def f(self, x):
        return 2 * x
print(A.f)      # <function A.f at 0x7f6ad882edc0>

''' Los comportamientos posteriores son confirmados por inspección: los métodos son reconocidos como funciones en 
Python 3'''
import inspect
print(inspect.isfunction(A.f))      # True
print(inspect.ismethod(A.f))        # False

''' En ambas versiones de Python, la función/método A.f puede ser llamada directamente, siempre que pases una instancia
 de la clase A como el primer argumento.'''

print(A.f(1, 7))        # 14
a = A()
print(A.f(a, 20))           # 40


''' Ahora supongamos que a es una instancia de la clase A, ¿qué es a.f entonces? Bueno, intuitivamente, esto debería 
ser el mismo método f de la clase A, solo que de alguna manera debería "saber" que fue aplicado al objeto a. 
En Python, esto se llama un método vinculado a a.'''

''' Los detalles más específicos son los siguientes: escribir a.f invoca el método mágico __getattribute__ de a, el 
cual primero verifica si a tiene un atributo llamado f (no lo tiene), luego verifica si la clase A contiene un método 
con ese nombre (sí lo tiene), y crea un nuevo objeto m de tipo method que tiene la referencia al original A.f en 
m.__func__, y una referencia al objeto a en m.__self__. Cuando este objeto se llama como una función, simplemente hace 
lo siguiente: m(...) => m.__func__(m.__self__, ...). Por lo tanto, este objeto se llama un método vinculado porque 
cuando se invoca sabe suministrar el objeto al que estaba vinculado como el primer argumento. '''

a = A()
print(a.f)              # <bound method A.f of <__main__.A object at 0x7fa7b4840dc0>>
print(a.f(2))           # 4

''' El objeto método vinculado a.f se recrea cada vez que lo llamas.'''
print(a.f is a.f)       # False

''' Como una optimización de rendimiento, puedes almacenar el método vinculado en el __dict__ del objeto, en cuyo caso
el objeto método permanecerá fijo '''
a.f = a.f
print(a.f is a.f)       # True


''' Finalmente, Python tiene métodos de clase y métodos estáticos, que son tipos especiales de métodos. Los métodos de 
clase funcionan de la misma manera que los métodos regulares, excepto que cuando se invocan en un objeto, se vinculan a 
la clase del objeto en lugar de al objeto. Así, m.__self__ = type(a). Cuando llamas a un método vinculado de este tipo, 
pasa la clase de a como el primer argumento. Los métodos estáticos son aún más simples: no vinculan nada en absoluto y 
simplemente devuelven la función subyacente sin ninguna transformación.'''


class D(object):
    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)


print(D.f)              # <bound method D.f of <class '__main__.D'>>
print(D.f(12))          # 24
print(D.g)              # <function D.g at 0x7fcfc84f5040>
print(D.g("world"))


''' Nota que los métodos de clase están vinculados a la clase incluso cuando se acceden desde la instancia'''
d = D()
d.multiplier = 1337
print((D.multiplier, d.multiplier))     # (2, 1337)

print(d.f)          # <bound method D.f of <class '__main__.D'>>

print(d.f(10))      # d.f(10)

''' Vale la pena señalar que, en el nivel más bajo, las funciones, métodos, métodos estáticos, etc., son en realidad 
descriptores que invocan los métodos especiales __get__, __set__ y opcionalmente __del__. Para más detalles sobre los 
métodos de clase y los métodos estáticos:'''

# https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

