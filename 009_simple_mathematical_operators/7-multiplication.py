import operator

'''

'''


def multiplication():
    a, b = 2, 3
    print(a * b)

    print(operator.mul(a, b))


    '''
    Posibles convinaciones

    int and int (dá un int )
    int and float (dá un float )
    int and complex (dá un complex )
    float and float (dá un float )
    float and complex (dá un complex )
    complex and complex (dá un complex )
    '''

    # Nota: El Operador * es tambien usado para repetir concatenacion de Strings, Listas y tuplas;
    print(3 * 'ab')  # = 'ababab'
    print(3 * ('a', 'b'))


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    multiplication()