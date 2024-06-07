'''
Python sigue la regla PEMDAS. PEMDAS significa paréntesis, exponentes, multiplicación y división y suma y resta.
'''
def precedence():
    a, b, c, d = 2, 3, 5, 7  # desempaquetado de variables
    print(a ** (b + c))     # parentesis

    print(a * b ** c)       # Exponente, lo mismo que  `a * (b ** c)`

    print(a + b * c / d)    # Multiplicacion / Division, Lo mismo que : `a + (b * c / d)`


    # Extras: mathematical rules hold, but not always:

    print(300 / 300 * 200)          # 200
    print(300 * 200 / 300)          # 200
    print(1e300 / 1e300 * 1e200)    # 1e+200
    print(1e300 * 1e200 / 1e300)    # inf

    '''
    El número "1e300" en Python representa 1 seguido de 300 ceros, lo que equivale a "1" multiplicado por "10" elevado 
    a la potencia de "300". Esto es una forma de notación científica en la que "e" indica la potencia de 10.
    '''


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    precedence()