'''
Función para solicitar al usuario un número
'''

def input_number(msg, err_msg=None):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            if err_msg is not None:
                print(err_msg)

# y usarlo
user_number = input_number("input a number: ", "that's not a number!")

# O si no deseas un "error message
#user_number = input_number("input a number: ")