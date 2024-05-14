'''
Para trabajar con enum es necesario instalar enum34
pip install enum34
'''

def function_creating_an_enum():
    from enum import Enum
    class Color(Enum):
        red = 1
        green = 2
        blue = 3

    print(Color.red)  # Color.red
    print(Color(1))  # Color.red
    print(Color['red'])  # Color.red
    print(Color.red.value)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_creating_an_enum()