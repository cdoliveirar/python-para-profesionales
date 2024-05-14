'''
El diccionario consta de pares clave-valor. Está encerrado entre llaves {} y se pueden asignar y acceder a los valores.
usando corchetes [].
'''


def function_parsing_string_timezone():
    # parsing a string with timezone into a datetime object is quick
    import dateutil.parser
    dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")
    print(dt)
    print("Tipo de objeto:")
    print(type(dt))             # <class 'datetime.datetime'>




# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_parsing_string_timezone()