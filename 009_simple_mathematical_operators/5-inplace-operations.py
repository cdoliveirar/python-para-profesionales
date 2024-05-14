import math

'''

'''


def inplace_operations():

    '''
    En las aplicaciones es comun hacer codigo como este;
    a = a + 1
    or
    a = a * 2

    Hay un efectivo shortcut para inplace operations:
    a += 1
    and
    a *= 2
    '''

    '''
    Cualquier operador matemático puede ser usado antes del caracter '=' para realizar un inplace operation
    
    -=  decrementa la variable en su lugar.
    +=  incrementa la variable en su lugar.
    *=  multiplica la variable en su lugar.
    /=  divide la variable en su lugar.
    //= divide la variable y redondea al entero más bajo en su lugar (división de piso) # Python 3
    %=  devuelve el módulo de la variable en su lugar.
    **= eleva a una potencia en su lugar.
    
    '''



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    inplace_operations()