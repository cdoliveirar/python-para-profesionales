'''
https://en.wikipedia.org/wiki/Short-circuit_evaluation
'''


'''
Evalua el primer argumento verdadero si cualquiera de los argumentos es verdadero. Si ambos argumentos 
son falsos evalua el segundo argumentyos
'''
def _or():
    x = True
    y = True
    z = x or y  # z = True
    print(z)

    x = True
    y = False
    z = x or y  # z = True
    print(z)

    x = False
    y = True
    z = x or y  # z = True
    print(z)

    x = False
    y = False
    z = x or y  # z = False
    print(z)

    x = 1
    y = 1
    z = x or y  # z = x, so z = 1, see `and` and `or` are not guaranteed to be a boolean
    print(z)

    x = 1
    y = 0
    z = x or y  # z = x, so z = 1 (see above)
    print(z)

    x = 0
    y = 1
    z = x or y  # z = y, so z = 1 (see above)
    print(z)

    x = 0
    y = 0
    z = x or y  # z = y, so z = 0 (see above)
    print(z)

    '''
    '1' puede ser cambiado por el valor True y 0 por el valor False
    '''

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    _or()