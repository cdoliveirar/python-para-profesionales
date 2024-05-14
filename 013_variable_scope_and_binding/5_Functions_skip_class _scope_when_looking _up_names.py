'''
Las clases tienen un ámbito local durante la definición, pero las funciones dentro de la clase no utilizan
ese ámbito al buscar nombres. Dado que las lambdas son funciones y las comprensiones se implementan usando
el ámbito de función, esto puede llevar a comportamientos sorprendentes.
'''

a = 'name global'

class Fred:
    a = 'class'                     # class scope
    b = (a for i in range(1))       # function scope
    c = [a for i in range(10)]      # function scope
    d = a                           # class scope
    e = lambda : a                  # function scope
    f = lambda a=a: a               # default argument uses class scope

    @staticmethod                   # or @classmethod, or regular instance method
    def g():                        # function scope
        return a


'''
https://stackoverflow.com/questions/13905741/accessing-class-variables-from-a-list-comprehension-in-the-class-definition/13913933#13913933
El ámbito de los nombres definidos en un bloque de clase se limita al bloque de clase; no se extiende a los bloques
de código de los métodos, esto incluye comprensiones y expresiones generadoras ya que se implementan utilizando un 
ámbito de función. Esto significa que lo siguiente fallará
'''

y = 3
class A:
    y = 42
    b = list(y + i for i in range(10))

print(Fred.a)               # class
print(next(Fred.b))         # global
print(Fred.c[1])            # class in Python 2, global in Python 3
print(Fred.c)               # global
print(Fred.d)               # class
print(Fred.e())             # global
print(Fred.f())             # class
print(Fred.g())             # global

print(A.b)


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


