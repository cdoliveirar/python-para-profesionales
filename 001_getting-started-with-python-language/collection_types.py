from collections import defaultdict
def function_collection_types():

    '''There are a number of collection types in Python. While types such as int and str hold a single value, collection
    types hold multiple values'''

    # Lists
    int_list = [1, 2, 3]
    string_list = ['abc', 'defghi']

    # A list can be empty:
    empty_list = []

    # The elements of a list are not restricted to a single data type, which makes sense given that Python is a dynamic
    # language:
    mixed_list = [1, 'abc', True, 2.34, None]

    # A list can contain another list as its element:
    nested_list = [['a', 'b', 'c'], [1, 2, 3]]
    names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
    print(names)
    print(names[0])  # Alice
    print(names[2])  # Craig

    # Indices can also be negative which means counting from the end of the list ( -1 being the index of the last element).
    # So, using the list from the above example:

    print(names[-1])  # Eric
    print(names[-4])  # Bob

    # Lists are mutable, so you can change the values in a list:
    names[0] = 'Ann'
    print(names)

    # Besides, it is possible to add and/or remove elements from a list:

    # Append object to end of list with L.append(object) , returns None .
    names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
    names.append("Sia")
    print(names)

    # Add a new element to list at a speciﬁc index. L.insert(index, object)
    names.insert(1, "Nikki")
    print(names)

    # Remove the ﬁrst occurrence of a value with L.remove(value) , returns None
    names.remove("Bob")
    print(names)

    # Get the index in the list of the ﬁrst item whose value is x. It will show an error if there is no such item.
    print(names.index("Alice"))

    # Count length of list: len()
    print(len(names))

    # count occurrence of any item in list
    a = [1, 1, 1, 2, 3, 4]
    print(a.count(1))

    # Reverse the list
    print(a.reverse())
    print(a[::-1])

    # Remove and return item at index (defaults to the last item) with L.pop([index]) , returns the item
    print(names.pop())

    # You can iterate over the list elements like below:
    for element in names:
        print(element)

    # TUPLES
    '''Una tupla es similar a una lista excepto que tiene una longitud fija y es inmutable. Entonces los valores en la
    tupla no se pueden cambiar. ni los valores se agregarán ni eliminarán de la tupla. Las tuplas se usan
    comúnmente para pequeñas colecciones de valores. que no será necesario cambiar, como la dirección IP y el puerto.
    Las tuplas se representan entre paréntesis en lugar de corchetes:'''

    ip_address = ('10.20.30.40', 8080)

    # Las mismas reglas de indexación para listas también se aplican a las tuplas. Las tuplas también se pueden
    # anidar y los valores pueden ser válidos. Python válido.

    # Una tupla con un solo miembro debe definirse (tenga en cuenta la coma) de esta manera
    one_member_tuple = ('Only member',)
    print(type(one_member_tuple))

    # ó

    one_member_tuple = 'Only member',      # No brackets
    print(type(one_member_tuple))

    # o simplemente usando la sintaxis de tupla
    one_member_tuple = tuple(['Only member'])
    print(type(one_member_tuple))

    # DICTIONARIES

    # Un diccionario en Python es una colección de pares clave-valor. El diccionario está rodeado de llaves. Cada par es
    # separados por una coma y la clave y el valor están separados por dos puntos.

    state_capitals = {
        'Arkansas': 'Little Rock',
        'Colorado': 'Denver',
        'California': 'Sacramento',
        'Georgia': 'Atlanta'
    }

    # Para obtener un valor, consúltelo por su clave:
    ca_capital = state_capitals['California']
    print(ca_capital)

    # También puedes obtener todas las claves en un diccionario y luego iterar sobre ellas
    for k in state_capitals.keys():
        print('{} is the capital of {}'.format(state_capitals[k], k))
        print('{} is the capital of {}'.format(k, k))

    # Los diccionarios se parecen mucho a la sintaxis JSON. El módulo json nativo de la biblioteca estándar de Python se puede utilizar para
    # convertir entre JSON y diccionarios.

    # SET
    '''Un conjunto es una colección de elementos sin repeticiones y sin orden de inserción pero sí ordenados.
    Se utilizan en Situaciones en las que sólo es importante que algunas cosas estén agrupadas y no el orden
    en que estaban incluido. Para grandes grupos de datos, es mucho más rápido verificar si un elemento 
    está o no en un conjunto que hacerlo lo mismo para una lista.'''

    # Definir un conjunto es muy similar a definir un diccionario

    first_names = {'Adam', 'Beth', 'Charlie'}
    print(first_names)

    # O puede crear un conjunto utilizando una lista existente
    my_list = [1, 2, 3]
    my_set = set(my_list)
    print(my_set)
    print(type(my_set))

    # Verifique la membresía del conjunto usando in:
    name = 'Adam'
    if name in first_names:
        print(name)

    # Puedes iterar sobre un conjunto exactamente como una lista, pero recuerda: los valores estarán en un orden
    # arbitrario definido por la implementación.

    # DEFAULTDICT
    '''Un defaultdict es un diccionario con un valor predeterminado para las claves, de modo que se pueda acceder
    sin errores a las claves para las que no se ha definido explícitamente ningún valor. defaultdict es
    especialmente útil cuando los valores en el diccionario son colecciones (list, dicts, etc.)
    en el sentido de que no es necesario inicializarlo cada vez que se usa una nueva clave.'''

    # Un defaultdict nunca generará un KeyError. Cualquier clave que no exista obtiene el valor predeterminado.
    state_capitals = {
        'Arkansas': 'Little Rock',
        'Colorado': 'Denver',
        'California': 'Sacramento',
        'Georgia': 'Atlanta'
    }

    # Si intentamos acceder a una clave inexistente, Python nos devuelve un error de la siguiente manera
    # print(state_capitals['Alabama'])  # KeyError: 'Alabama'

    # Intentemos con un defaultdict. Se puede encontrar en el módulo de colecciones.
    # from collections import defaultdict  # se importo en la primera linea del fichero
    state_capitals = defaultdict(lambda: 'Puc')

    # Lo que hicimos aquí es establecer un valor predeterminado (Puc) en caso de que la clave proporcionada
    # no exista. Ahora complete el dictado como antes:

    state_capitals['Arkansas'] = 'Little Rock'
    state_capitals['California'] = 'Sacramento'
    state_capitals['Colorado'] = 'Denver'
    state_capitals['Georgia'] = 'Atlanta'

    # Si intentamos acceder al dict con una clave inexistente, Python nos devolverá el valor predeterminado,
    # es decir, Puc.
    print(state_capitals['Ucayali'])

    # y devuelve los valores creados para la clave existente como un diccionario normal
    print(state_capitals['Arkansas'])




# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_collection_types()
