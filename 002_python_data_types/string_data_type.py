'''
Las cadenas se identifican como un conjunto contiguo de caracteres representados entre comillas. Python permite
cualquiera de las dos pares de comillas simples o dobles. Las cadenas son un tipo de datos de secuencia inmutable,
es decir, cada vez que se realizan cambios a una cadena, se crea un objeto de cadena completamente nuevo.
'''

def function_string_data_types():

    a_str = 'Hello World'
    print(a_str)        # output will be whole string. Hello World
    print(a_str[0])     # output will be first character. H
    print(a_str[0:5])   # output will be first five characters. Hello

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_string_data_types()