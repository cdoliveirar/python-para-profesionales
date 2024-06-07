'''
Funciones (En línea/Anónimas) Lambda
'''

''' La palabra clave lambda crea una función en línea que contiene una única expresión. El valor de esta expresión es 
lo que la función devuelve cuando se invoca.'''

# Considerar la funcion
def greeting():
    return "Hello"

# que, cuando se llama como:
print(greeting())

# imprime:  # Hello

''' Esto se puede escribir como una función lambda de la siguiente manera: '''
greet_me = lambda: "Hello"

'''  Esto crea una función en línea con el nombre greet_me que devuelve "Hello". Ten en cuenta que no escribes return 
al crear una función con lambda. El valor después de : se devuelve automáticamente.

Una vez asignada a una variable, se puede usar como una función regular
'''
print(greet_me())   # Hello

# Lambdas puede tomar argumentos tambien:
strip_and_upper_case = lambda s: s.strip().upper()
print(strip_and_upper_case("   Hello        "))         # HELLO

''' También pueden tomar un número arbitrario de argumentos / argumentos con nombre, como las funciones normales.'''
greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')
# hello ('world',) {'world': 'world'}

''' Las lambdas se usan comúnmente para funciones cortas que son convenientes de definir en el punto donde se llaman 
(típicamente con sorted, filter y map).'''

''' Por ejemplo, esta línea ordena una lista de cadenas ignorando mayúsculas y minúsculas y los espacios en blanco al 
principio y al final:'''
print(sorted( [" foo ", "bAR", "BaZ "], key=lambda s: s.strip().upper())) #  ['bAR', 'BaZ ', ' foo ']

''' Ordenar lista ignorando solo los espacios en blanco '''
print(sorted( [" foo ", "bAR", "BaZ "], key=lambda s: s.strip()))


# Ejmeplos con Map
print(sorted(map( lambda s: s.strip().upper(), [" foo ", "   bAR", "BaZ   "])))
# ['BAR', 'BAZ', 'FOO']

print(sorted( map( lambda s: s.strip(), [" foo ", "   bAR", "BaZ   "])))
# ['BaZ', 'bAR', 'foo']


# Ejemplos con listas numericas
my_list = [3, -4, -2, 5, 1, 7]
print(sorted( my_list, key=lambda x: abs(x)))       # [1, -2, 3, -4, 5, 7]

print(list(filter( lambda x: x>0, my_list)))       # [3, 5, 1, 7]
''' estamos generando una nueva lista que contiene los valores absolutos de los elementos originales de my_list'''

print(list(map( lambda x: abs(x), my_list)))       # [3, 4, 2, 5, 1, 7]


''' Uno puede llamar otras funciones (con/sin argumentos) desde dentro de una función lambda.'''
def foo(msg):
    print(msg)

greet = lambda x = "hello world": foo(x)

greet()         # hello world

''' Esto es útil porque lambda puede contener solo una expresión y al usar una función subsidiaria se pueden ejecutar 
múltiples declaraciones.'''


'''
NOTA

Siempre usa una declaración def en lugar de una declaración de asignación que enlace directamente una expresión lambda 
a un identificador.

SI
def f(x): return 2*x

NO
f = lambda x: 2*x

La primera forma significa que el nombre del objeto de función resultante es específicamente f en lugar del genérico 
<lambda>. Esto es más útil para trazas de errores y representaciones de cadena en general. El uso de la declaración 
de asignación elimina el único beneficio que una expresión lambda puede ofrecer sobre una declaración def explícita 
(es decir, que puede estar incrustada dentro de una expresión más grande).
'''






