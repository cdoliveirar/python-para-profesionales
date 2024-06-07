'''
Definiendo una función con un número arbitrario de argumentos
'''

''' 
Número arbitrario de argumentos posicionales 
'''

''' Definir una función capaz de tomar un número arbitrario de argumentos se puede hacer anteponiendo un * a uno de 
los argumentos.'''
def func(*args):
# args will be a tuple containing all values that are passed in
    for i in args:
        print(i)

# llmando con 3 argumentos
func(1, 2, 3)
# 1
# 2
# 3

list_of_arg_values = [1, 2, 3]
func(*list_of_arg_values)       # Llamarla con una lista de valores, * expande la lista.
# 1
# 2
# 3
''' No puedes proporcionar un valor predeterminado para args, por ejemplo func(*args=[1, 2, 3]) generará un error de 
sintaxis (ni siquiera se compilará).

No puedes proporcionarlos por nombre al llamar a la función, por ejemplo func(*args=[1, 2, 3]) generará un TypeError.

Pero si ya tienes tus argumentos en un array (o en cualquier otro Iterable), puedes invocar tu función así: 
func(*my_stuff).

Estos argumentos (*args) se pueden acceder por índice, por ejemplo, args[0] devolverá el primer argumento.
'''


''' 
Número arbitrario de keyword argumentos 
'''
''' Puedes tomar un número arbitrario de argumentos con nombre definiendo un argumento en la definición con 
dos ** delante de él.'''
def func(**kwargs):
# kwargs será un diccionario que contiene los name como claves y los value como valores.
    for name, value in kwargs.items():
        print(name, value)

func(value1=1, value2=2, value3=3)
# value1 1
# value2 2
# value3 3

my_dict = {'foo': 1, 'bar': 2}
func(**my_dict)
# foo 1
# bar 2
''' No puedes proporcionar estos sin nombres, por ejemplo, func(1, 2, 3) generará un TypeError.'''
''' kwargs es un diccionario nativo de Python. Por ejemplo, args['value1'] te dará el valor del argumento value1. 
Asegúrate de verificar de antemano que existe tal argumento o se generará un KeyError.'''

'''Advertencia'''
''' Puedes mezclar estos con otros argumentos opcionales y requeridos, pero el orden dentro de la definición importa.'''
''' 
* Primero vienen los argumentos posicionales/keyword "positional/keyword" (argumentos requeridos).
* Luego vienen los argumentos arbitrarios *arg "arbitrary" (opcionales).
* Luego vienen los argumentos solo con nombre "keyword-only" (requeridos).
* Finalmente, vienen los argumentos con nombre arbitrarios **kwargs "arbitrary keyword"  (opcionales).
'''

#       |-positional-|-optional-|---keyword-only--|-optional-|
def func(arg1, arg2=10 , *args, kwarg1, kwarg2=2, **kwargs):
    pass

'''
- arg1 debe ser proporcionado, de lo contrario se genera un TypeError. Puede ser dado como un argumento posicional 
(func(10)) o como un argumento con nombre (func(arg1=10)).

- kwarg1 también debe ser proporcionado, pero solo puede ser dado como un argumento con nombre: func(kwarg1=10).

- arg2 y kwarg2 son opcionales. Si se va a cambiar el valor, se aplican las mismas reglas que para arg1 (ya sea 
posicional o con nombre) y kwarg1 (solo con nombre).

- *args captura parámetros posicionales adicionales. Pero ten en cuenta que arg1 y arg2 deben ser proporcionados como 
argumentos posicionales para pasar argumentos a *args: func(1, 1, 1, 1).

- **kwargs captura todos los parámetros con nombre adicionales. En este caso, cualquier parámetro que no sea arg1, 
arg2, kwarg1 o kwarg2. Por ejemplo: func(kwarg3=10).

- En Python 3, puedes usar * solo para indicar que todos los argumentos subsecuentes deben ser especificados como 
argumentos con nombre.
Por ejemplo, la función math.isclose en Python 3.5 y versiones superiores se define usando def math.isclose(a, b, *, 
rel_tol=1e-09, abs_tol=0.0), lo que significa que los dos primeros argumentos pueden ser proporcionados de manera 
posicional, pero los parámetros opcionales tercero y cuarto solo pueden ser proporcionados como argumentos con nombre.
'''

''' 
Nota sobre la nomenclatura:

La convención de nombrar los argumentos posicionales opcionales como args y los argumentos con nombre opcionales como 
kwargs es solo una convención. Puedes usar cualquier nombre que prefieras, pero es útil seguir la convención para 
que otros sepan lo que estás haciendo, o incluso para que tú mismo lo sepas más tarde,  sigue la convención.
'''

''' 
Nota sobre la unicidad

Cualquier función puede definirse sin o con un *args y sin o con un **kwargs, pero no con más de uno de cada uno. 
Además, *args debe ser el último argumento posicional y **kwargs debe ser el último parámetro. Intentar usar más de 
uno de cada uno resultará en una excepción de Syntax Error.
'''

'''
Nota sobre anidar funciones con argumentos opcionales

Es posible anidar tales funciones y la convención habitual es eliminar los elementos que el código ya ha manejado, 
pero si estás pasando los parámetros, necesitas pasar los argumentos posicionales opcionales con un prefijo * y los 
argumentos con nombre opcionales con un prefijo **, de lo contrario, args se pasarán como una lista o tupla y kwargs 
como un único diccionario. Por ejemplo:
'''

def fn(**kwargs):
    print(kwargs)
    f1(**kwargs)

def f1(**kwargs):
    print(len(kwargs))

fn(a=1, b=2)