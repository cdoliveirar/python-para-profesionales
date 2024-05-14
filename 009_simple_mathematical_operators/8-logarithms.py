import math
import cmath
'''

'''


def logarithms():
    '''
    Por defecto, la función math.log calcula el logaritmo de un número en base e. Opcionalmente, puedes especificar
    una base como segundo argumento.
    '''

    print(math.log(5))
    # = 1.6094379124341003
    # optional base argument. Default is math.e
    print(math.log(5, math.e))  # = 1.6094379124341003
    print(cmath.log(5))
    # = (1.6094379124341003+0j)
    print(math.log(1000, 10))   # 2.9999999999999996
    # 3.0 (always returns float)
    print(cmath.log(1000, 10))  # (3+0j)

    '''
    Existen variaciones especiales de la función math.log para diferentes bases
    '''
    # Logarithm base e - 1 (higher precision for low values)
    print(math.log1p(5))    # = 1.791759469228055
    # Logarithm base 2
    print(math.log2(8))         # = 3.0
    # Logarithm base 10
    print(math.log10(100))      # = 2.0
    print(cmath.log10(100))     # = (2+0j)


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    logarithms()