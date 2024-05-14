from __future__ import division
from operator import truediv
import operator

'''

'''
import __future__
from enum import Enum



def division():
    a, b, c, d, e = 3, 2, 2.0, -3, 10

    print(a / b)
    print(a / c)
    print(d / b)
    print(b / a)
    print(d / e)

    # no es necesario el operador en python 3
    #import operator
    #operator.div(a, b)


    print(a // b)

    print(a / (b * 1.0))
    print(a / b * 1.0)

    # true divide
    print("truediv: %s" % truediv(a, b))

    print(float(a) / b)
    print(a / float(b))

    x,y = 20,6
    # // duvussion entera dando resultado un entero más cercano hacia abajo.
    print("x//y: ")
    print(x//y)

    # provemos un modulo
    print("x%y:")
    print(x%y)


    print(operator.truediv(x,y))
    print(operator.floordiv(x, y))



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    division()