def function_set_data_types():

    # Los conjuntos son colecciones desordenadas de objetos únicos, existen dos tipos de conjuntos

    # 1. SETS: Son mutables y se pueden agregar nuevos elementos una vez que se definen los conjuntos.
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)     # duplicates will be removed

    a = set('abracadabra')
    print(a)
    print(dir(a))           # verificar los metodos

    a.add('z')
    print(a)

    # 2. Frozen Sets - Son inmutables y no se pueden agregar nuevos elementos después de su definición.
    b = frozenset('asdfagsa')
    print(b)

    cities = frozenset(["Frankfurt", "Basel", "Freiburg"])
    print(cities)
    print(dir(cities))      # verificar los metodos


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_set_data_types()
