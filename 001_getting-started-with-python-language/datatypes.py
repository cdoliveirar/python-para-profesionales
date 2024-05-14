
def function_datatypes():
    # Booleans
    # bool : A boolean value of either True or False. Logical operations like and , or , not can be performed on booleans.

    # x or y      # if x is False then y otherwise x
    # x and y     # if x is False then x otherwise y
    # not x       # if x is True then False, otherwise True

    print(issubclass(bool, int))
    print(isinstance(True, bool))
    print(isinstance(False, bool))

    print(True + False)
    print(True * True)

    # Numbers
    # int : Integer number

    a = 2
    b = 100
    c = 123456789
    d = 38563846326424324

    '''float: Floating point number; precision depends on the implementation and system architecture, for CPython
    the float datatype corresponds to a C double.'''

    a = 2.0
    b = 100.e0
    c = 123456789.e1

    # complex : Complex numbers
    a = 2 + 1j
    b = 100 + 10j

    # Sequences and collections
    # Python diﬀerentiates between ordered sequences and unordered collections (such as set and dict ).

    # strings ( str , bytes , unicode ) are sequences
    # reversed : A reversed order of str with reversed function

    a = reversed('hello')
    print(list(a))

    # TUPLE: An ordered collection of n values of any type(n >= 0)
    # Supports indexing; immutable; hashable if all its members are hashable

    a = (1, 2, 3)
    b = ('a', 1, 'python', (1, 2))
    # b[2] = 'something else'  # returns a TypeError
    # TypeError: 'tuple' object does not support item assignment


    # LIST: An ordered collection of n values(n >= 0)
    # Not hashable; mutable.

    a = [1, 2, 3]
    b = ['a', 1, 'python', (1, 2), [1, 2]]
    b[2] = 'something else'  # allowed

    print(b)

    # SET: An unordered collection of unique values.Items must be hashable.
    # sin embargo se puede agregar o elminar elementos del conjunto
    a = {1, 2, 'a'}

    # DICT : An unordered collection of unique key-value pairs; keys must be hashable.
    # los keys son inmutables, pero se puede actualizar el valor de una llave especifica.

    a = {1: 'one', 2: 'two'}
    b = {'a': [1, 2, 3], 'b': 'a string'}

    # Testing the type of variables
    # In python, we can check the datatype of an object using the built-in function type .
    a = '123'
    print(type(a))

    '''En declaraciones condicionales es posible probar el tipo de datos con isinstance. Sin embargo, generalmente
    no se recomienda depender del tipo de variable.'''

    i = 7
    if isinstance(i, int):
        i += 1
    elif isinstance(i, str):
        i = int(i)
        i += 1
    print(i)


    # To test if something is of NoneType :
    x = None
    if x is None:
        print('Not a surprise, I just defined x as None.')

    # Converting between datatypes

    # You can perform explicit datatype conversion.
    # For example, '123' is of str type and it can be converted to integer using int function.
    a = '123'
    b = int(a)

    # Converting from a ﬂoat string such as '123.456' can be done using float function.
    a = '123.456'
    b = float(a)
    # c = int(a)      # ValueError: invalid literal for int() with base 10: '123.456'
    d = int(b)
    # en este caso pasar primero de floar a int!

    # You can also convert sequence or collection types
    a = 'hello'
    list(a)     # ['h', 'e', 'l', 'l', 'o']
    set(a)      # {'o', 'e', 'l', 'h'}
    tuple(a)    # ('h', 'e', 'l', 'l', 'o')

    # Mutable and Immutable Data Types
    '''An object is called mutable if it can be changed. For example, when you pass a list to some function, the  list
    can be changed'''

    def f(m):
        m.append(3)

    x = [1, 2]
    f(x)
    print(x == [1, 2])  #False, desde que se agregó un elemento a la lista

    # An object is called immutable if it cannot be changed in any way. For example, integers are immutable,
    # since there's no way to change them:

    # Examples of immutable Data Types:
        # int, long, float, complex
        # str
        # bytes
        # tuple
        # frozenset

    # Examples of mutable Data Types:
        # bytearray
        # list
        # set
        # dict




# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_datatypes()
