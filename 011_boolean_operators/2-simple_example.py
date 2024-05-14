'''
En Python puedes comparar un solo elemento usando dos operadores binarios, uno en cada lado:
'''


def simple_example():
    x=3.141
    if 3.14 < x < 3.142:
        print("x is near pi")


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    simple_example()