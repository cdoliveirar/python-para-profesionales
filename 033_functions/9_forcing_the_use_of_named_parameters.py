'''
Forzar el uso de parámetros con nombre
'''

''' Todos los parámetros especificados después del primer asterisco (*) en la firma de la función son exclusivos de 
palabra clave (keyword-only)'''

def f(*a, b):
    pass

#f(1, 2, 3) # TypeError: f() missing 1 required keyword-only argument: 'b'

''' es posible colocar un solo asterisco en la firma de la función para asegurar que los argumentos restantes solo 
puedan pasarse utilizando argumentos de palabra clave.'''
def g(a, b, *, c):
    pass
# g(1, 2, 3)      # TypeError: g() takes 2 positional arguments but 3 were given

g(1, 2, c=3)    # No hay error

