'''
Parametros                  Detalle
f                           La función a ser decorada "envuelta" ((wrapped))
'''

'''
Las funciones decoradoras son patrones de diseño de software. Alteran dinámicamente la funcionalidad de una función, 
método o clase sin tener que usar directamente subclases o cambiar el código fuente de la función decorada. Cuando se 
usan correctamente, los decoradores pueden convertirse en herramientas poderosas en el proceso de desarrollo. 
vamos abarcar la implementación y aplicaciones de las funciones decoradoras en Python.
'''

''' Los decoradores aumentan el comportamiento de otras funciones o métodos. Cualquier función que tome una función 
como parámetro y devuelva una función aumentada puede ser utilizada como un decorador'''

# Este decorador más simple no hace nada a la función que está siendo decorada. Decoradores tan mínimos pueden ser
# usados ocasionalmente como una especie de marcadores de código.
def super_secret_function(f):
    return f

@super_secret_function
def my_function():
    print("This is my secret function.")

''' La notación @ es sintácticamene que es equivalente a lo siguiente.'''
my_function = super_secret_function(my_function)

''' Es importante tener esto en cuenta para entender cómo funcionan los decoradores. Esta sintaxis "sin azúcar" deja 
claro por qué la función decoradora toma una función como argumento y por qué debería devolver otra función. 
También demuestra lo que sucedería si no devuelves una función. '''
def disabled(f):
    """
    Esta función no devuelve nada y, por lo tanto, elimina la función decorada del ámbito local.
    """
    pass

@disabled
def my_function():
    print("This function can no longer be called...")


# print(my_function())        # TypeError: 'NoneType' object is not callable
''' cuando intentas imprimir el resultado de llamar a my_function(), realmente estás llamando a None(), lo cual produce 
un error de tipo TypeError porque None no es invocable.'''

''' Así, generalmente definimos una nueva función dentro del decorador y la devolvemos. Esta nueva función primero 
haría algo que necesite hacer, luego llamaría a la función original y finalmente procesaría el valor de retorno. 

Considera esta función decoradora simple que imprime los argumentos que recibe la función original y luego la llama.'''

# Este es el decorador
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)    # Llama a la función original con sus argumentos
    return inner_func

@print_args
def multiply(num_a, num_b, a = 3):
    return num_a * num_b


print(multiply(3, 5))
# (3, 5)        # Esto es en realidad los 'args' que la función recibe : print(args)
# {}            # sto son los 'kwargs', vacíos porque no especificamos argumentos de palabras clave: print(kwargs)
# 15            # El resultado de la funcion.

