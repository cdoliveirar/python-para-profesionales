def function_creating_variables():
    # Use a breakpoint in the code line below to debug your script.
    # Integer
    a = 2
    print(a)
    b = 9223372036854775807
    print(b)

    # Floating point
    pi = 3.14
    print(pi)
    # Output: 3.14

    # String
    c = 'A'
    print(c)
    # Output: A

    # String
    name = 'John Doe'
    print(name)
    # Output: John Doe

    # Boolean
    q = True
    print(q)
    # Output: True

    # Empty value or null data type
    x = None
    print(x)
    # Output: None

    #Variable assignment works from left to right.So the following will give you an syntax error.
    #0 = x
    #SyntaxError: cannot assign to literal


    #Rules for variable naming:

    #- - - - - - - - - - - - - - - - - - - - -

    # 1. Variables names must start with a letter or an underscore.
    x = True    # valid
    _y = True   # valid

    #9x = False  # starts with numeral
    # SyntaxError: invalid syntax

    # $y = False  # starts with symbol
    # SyntaxError: invalid syntax

    # 2. The remainder of your variable name may consist of letters, numbers and underscores.
    has_0_in_it = "Still Valid"

    # 3. Names are case sensitive.

    # x = 9
    # y = X * 5
    # NameError: name 'X' is not defined

    # - - - - - - - - - - - - - - - - - - - - -
    '''Aunque no es necesario especificar un tipo de datos al declarar una variable en Python, al asignar el área
    necesaria en la memoria para la variable, el intérprete de Python selecciona automáticamente la función
    incorporada más adecuada.'''


    a = 2
    print(type(a))

    b = 9223372036854775807
    print(type(b))

    pi = 3.14
    print(type(pi))

    c = 'A'
    print(type(c))

    name = 'John Doe'
    print(type(name))

    q = True
    print(type(q))

    x = None
    print(type(x))

    '''Ahora que conoce los conceptos básicos de la asignación, dejemos de lado esta sutileza sobre la asignación
    en Python.
    Cuando usas = para realizar una operación de asignación, lo que hay a la izquierda de = es el nombre del objeto
    a la derecha. Finalmente, lo que = hace es asignar la referencia del objeto de la derecha al nombre de  la
    izquierda.'''

    # a_name = an_object  # "a_name" is now a name for the reference to the object "an_object"

    a, b, c = 1, 2, 3
    print(a, b, c)

    # a, b, c = 1, 2
    # ValueError: not enough values to unpack (expected 3, got 2)

    # a, b = 1, 2, 3
    # ValueError: too many values to unpack (expected 2)

    '''El error del último ejemplo se puede evitar asignando los valores restantes a un número igual de variables
    arbitrarias.
    Esta variable ficticia puede tener cualquier nombre, pero es convencional utilizar el guión bajo(_)  para asignar
    variables no deseadas'''

    a, b, _ = 1, 2, 3
    print(a, b)

    a = b = c = 1
    print(a, b, c)

    '''Cuando se utiliza dicha asignación en cascada, es importante tener en cuenta que las tres variables a, b y c
    se refieren a la misma objeto en la memoria, un objeto int con el valor de 1. En otras palabras, a, b y c
    son tres nombres diferentes dados al mismo objeto int. Asignar posteriormente un objeto diferente a uno de
    ellos no cambia los demás, tal como se esperaba:'''

    a = b = c = 1   # all three names a, b and c refer to same int object with value 1
    print(a, b, c)

    b = 2       # b now refers to another int object, one with a value of 2
    print(a, b, c)

    '''Lo anterior también es válido para tipos mutables(como list, dict, etc.), al igual que lo es para tipos 
    inmutables(como int, string, tupla, etc.):'''

    x = y = [7, 8, 9]   # x and y refer to the same list object just created, [7, 8, 9]
    x = [13, 8, 9]      # x now refers to a different list object just created, [13, 8, 9]
    print(y)            # y still refers to the list it was first assigned

    '''Hasta ahora, todo bien.Las cosas son un poco diferentes cuando se trata de modificar el objeto(en contraste con
    asignar el nombre a un objeto diferente, lo cual hicimos anteriormente) cuando la asignación en cascada se usa
    para tipos mutables.Echar un vistazo a continuación, y lo verás de primera mano:'''

    x = y = [7, 8, 9]       # x and y are two different names for the same list object just created, [7, 8, 9]
    x[0] = 13               # we are updating the value of the list [7, 8, 9] through one of its names, x in this case
    print(y)                # printing the value of the list using its other name

    '''Las listas anidadas también son válidas en Python. Esto significa que una lista puede contener otra lista
    como elemento.'''

    x = [1, 2, [3, 4, 5], 6, 7]     # this is nested list
    print(x[2])
    print(x[2][1])

    '''Lastly, variables in Python do not have to stay the same type as which they were ﬁrst deﬁned - - you can simply
    use = to assign a new value to a variable, even if that value is of a diﬀerent type.'''

    a = 2
    print(a)

    a = "New value"
    print(a)

    '''Si esto te molesta, piensa en el hecho de que lo que hay a la izquierda de = es sólo el nombre de un
    objeto. Primero llamas al int objeto con valor 2 a, luego cambias de opinión y decides darle el nombre
    a a un objeto de cadena, que tiene valor 'Nuevo valor'.Sencillo, ¿verdad?'''

    

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_creating_variables()

