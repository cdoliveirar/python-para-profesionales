'''
Una lista contiene elementos separados por comas y encerrados entre corchetes []. Las listas son casi similares
a las matrices en C. Una diferencia es que todos los elementos que pertenecen a una lista pueden ser de
diferentes tipos de datos.
'''


def function_list_data_type():

    list = [123, 'abcd', 10.2, 'd']     # can be an array of any data type or single data type.
    list1 = ['hello', 'world']
    print(list)                         # will output whole list. [123,'abcd',10.2,'d']
    print(list[0:2])                    # will output first two element of list. [123,'abcd']
    print(list1 * 2)                    # will gave list1 two times. ['hello','world','hello','world']
    print(list + list1)                 # will gave concatenation of both the lists.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_list_data_type()