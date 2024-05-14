import operator
import math
'''

'''

def exponentiation():
    a, b = 2, 3
    print(a ** b)
    # pow
    print(pow(a, b))

    # Con Match
    print(math.pow(a, b))

    # Con operator
    print(operator.pow(a, b))

    # Otra diferencia entre build-in pow y match.pow es que el build-in pow puede aceptar 3 argumentos:
    a, b, c = 2, 3, 2
    print(pow(2, 3, 2))     # 0, calculates (2 ** 3) % 2, but as per Python docs,
    # el % calcula el modulo del resultado 2 exponente 3 que es 8, entonces 8 modulo 2 es 0 ya que el residuo es 0


    #   Funciones especiales
    # Raiz Cuadrada
    # The function math.sqrt(x) calculates the square root of x.

    import cmath
    c = 4
    print(math.sqrt(c))         # = 2.0 (always float; does not allow complex results)
    print(cmath.sqrt(c))        # = (2+0j) (always complex)

    x = 8
    print(math.pow(x, 1 / 3))   # 2.0, el resulltado se refiere a 2 elevado a 3 = 8
    print(x**(1/3))             # 2.0, el resulltado se refiere a 2 elevado a 3 = 8

    # e = logaritmo natural (aproximadamente 2.71828 )
    # The function math.exp(x) computes e ** x.

    print(math.exp(0))    # 1.0
    print(math.exp(1))    # 2.718281828459045 (e)

    #The function math.expm1(x) computes e ** x - 1.When x is small, this gives signiﬁcantly better  precision than
    # math.exp(x) - 1.
    print(math.exp(x) - 1)  # 0.0

    print(math.expm1(0))

    print(math.exp(1e-6) - 1)
    print(math.expm1(1e-6))






if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    exponentiation()