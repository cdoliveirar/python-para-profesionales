'''
Enums are iterable:
'''
from enum import Enum


def function_iteration():
    class Color(Enum):
        red = 1
        green = 2
        blue = 3
    print([c for c in Color])


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_iteration()