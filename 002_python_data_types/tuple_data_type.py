'''
Las listas están entre paréntesis [ ] y sus elementos y tamaño se pueden cambiar, mientras que las
tuplas están entre paréntesis ( ) y no se pueden actualizar. Las tuplas son inmutables.
'''

def function_string_data_types():

    tuple = (123, 'hello')
    tuple1 = ('world',)
    otra_forma_tuple = 'hola',
    concatena_tupla= tuple + tuple1
    print(otra_forma_tuple)
    print(tuple)            # will output whole tuple. (123,'hello')
    print(tuple[0])         # will output first value. (123)
    print(tuple + tuple1)   # will output (123,'hello','world')
    print(concatena_tupla)
    #tuple[1] = 'update'     # this will give you error.

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_string_data_types()