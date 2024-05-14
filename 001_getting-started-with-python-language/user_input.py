def function_user_input():
    # Interactive input
    name = input("What is your name? ")
    print(name)

    # Tenga en cuenta que la entrada siempre es de tipo str , lo cual es importante si desea que el usuario
    # ingrese números. Por lo tanto, necesitas convertir la cadena antes de intentar usarla como un número:

    x = input("Write a number:")
    # x / 2  # TypeError: unsupported operand type(s) for /: 'str' and 'int'

    print( float(x) / 2 )

    # It's recommended to use try / except blocks to catch exceptions when dealing with user inputs

   
# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_user_input()