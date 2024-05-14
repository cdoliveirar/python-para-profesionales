import operator
'''

'''


def modulus():
    '''
    Como en muchos otros lenguajes, Python utiliza el operador % para calcular el módulo
    '''

    print(3 % 4)       # 3
    print(10 % 2)      # 0
    print(6 % 4)       # 2

    # usando el modulo operador
    print(operator.mod(3, 4))
    print(operator.mod(10, 2))
    print(operator.mod(6, 4))

    # Tambein puede ser usado en numeros negativos.
    '''
    -9 % 7  # 5
    9 % -7  # -5
    -9 % -7 # -2
    '''

    '''
    Si necesitas encontrar el resultado de la división entera y el módulo, puedes usar la función divmod como un atajo
    '''
    print("imprimir conciente y resto")
    quotient, remainder = divmod(9, 4)
    print("Conciente: ", quotient)
    print("Residuo: ", remainder)

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    modulus()