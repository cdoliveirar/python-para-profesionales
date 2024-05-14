'''
Devuelve lo contrario de las siguienbtes declaraciones
'''


def _not():
    x = True
    y = not x  # y = False
    print(y)

    x = False
    y = not x  # y = True
    print(y)




if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    _not()