'''
https://en.wikipedia.org/wiki/Short-circuit_evaluation
'''


'''
Evalúa  el segundo argumento si y solo si ambos argumentos son verdaderos. De lo contrario, 
se evalúa como el primer argumento falso.
'''
def _and():
    x = True
    y = True
    z = x and y  # z = True
    print(z)

    x = True
    y = False
    z = x and y  # z = False
    print(z)

    x = False
    y = True
    z = x and y  # z = False
    print(z)

    x = False
    y = False
    z = x and y  # z = False
    print(z)

    x = 1
    y = 1
    z = x and y  # z = y, so z = 1, see `and` and `or` are not guaranteed to be a boolean
    print(z)

    x = 0
    y = 1
    z = x and y  # z = x, so z = 0 (see above)
    print(z)

    x = 1
    y = 0
    z = x and y  # z = y, so z = 0 (see above)
    print(z)

    x = 0
    y = 0
    z = x and y  # z = x, so z = 0 (see above)
    print(z)







if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    _and()