import operator

'''

'''


def subtraction():
    a, b = 1, 2
    # Usando el operador"-":
    print(b-a)

    print(operator.sub(b,a))

    '''
    Posibles convinaciones
    
    int and int (dá un int )
    int and float (dá un float )
    int and complex (dá un complex )
    float and float (dá un float )
    float and complex (dá un complex )
    complex and complex (dá un complex )
    
    '''



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    subtraction()