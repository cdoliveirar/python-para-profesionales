'''
Parametros                      Detalles
arg1, ..., argN                 Argumentos regulares
*args                           Argumentos posicionales sin nombre
kw1, ..., kwN                   Argumentos solo de palabra clave (Keyword-only arguments)
**kwargs                        El resto de los argumentos de palabra clave (keyword arguments)
'''

''' 
Las funciones en Python proporcionan un código organizado, reutilizable y modular para realizar un conjunto de acciones
específicas. Las funciones simplifican el proceso de codificación, previenen la lógica redundante y hacen que el código 
sea más fácil de seguir. vamos a describir la declaración y utilización de funciones en Python.'''

''' Python tiene muchas funciones integradas como print(), input(), len(). Además de las funciones integradas 
(built-ins), también puedes crear tus propias funciones para realizar trabajos más específicos; estas se llaman 
funciones definidas por el usuario (user-deﬁned functions).'''

'''
Usar la declaración def es la forma más común de definir una función en Python. Esta declaración es una llamada 
declaración compuesta de una sola cláusula (single clause compound statement)con la siguiente sintaxis:
'''


def function_name(parameters):
    pass    # statement(s)


''' nombre_de_la_función se conoce como el identificador de la función. Dado que una definición de función es una 
declaración ejecutable, su ejecución vincula el nombre de la función al objeto de la función, el cual puede ser 
llamado posteriormente usando el identificador.'''

''' parámetros es una lista opcional de identificadores que se vinculan a los valores suministrados como argumentos 
cuando se llama a la función. Una función puede tener un número arbitrario de argumentos que se separan por comas.'''

''' declaración(es) – también conocido como el cuerpo de la función – es una secuencia no vacía de declaraciones que 
se ejecutan cada vez que se llama a la función. Esto significa que el cuerpo de una función no puede estar vacío, 
al igual que cualquier bloque indentado.'''

'''Aquí hay un ejemplo de una definición de función simple cuyo propósito es imprimir "Hello" cada vez que se llama:'''

def saludar():
    print("Hello")


''' Ese es otro ejemplo de una definición de función que toma un solo argumento y muestra el valor pasado cada vez que 
se llama a la función.'''
def greet_two(greeting):
    print(greeting)


''' También puedes dar un valor predeterminado a ese argumento de la función:'''
def greet_three(greeting="Howdy"):
    print(greeting)

''' Notarás que, a diferencia de muchos otros lenguajes, no necesitas declarar explícitamente un tipo de retorno para 
la función. Las funciones en Python pueden devolver valores de cualquier tipo mediante la palabra clave return. ¡Una 
función puede devolver cualquier número de tipos diferentes!'''
def many_types(x):
    if x < 0:
        return "Hello!"
    else:
        return 0

print(many_types(1))    # 0
print(many_types(-1))   # Hello!

''' Mientras esto sea manejado correctamente por quien llama a la función, este es código Python perfectamente 
válido.'''

''' Una función que llega al final de su ejecución sin una declaración return siempre devolverá None:'''
def do_nothing():
    pass
print(do_nothing())     # None

''' Como se mencionó anteriormente, una definición de función debe tener un cuerpo de función, una secuencia no vacía 
de declaraciones. Por lo tanto, la declaración pass se usa como cuerpo de la función, lo cual es una operación nula: 
cuando se ejecuta, no pasa nada. 
Hace lo que significa, se salta. Es útil como un marcador de posición cuando se requiere una declaración 
sintácticamente, pero no se necesita ejecutar ningún código.'''

# Ahora llamemos a la función a las funciones definidas
saludar()
# llamamos con un argumento.
greet_two("Benj")
#Ahora puedes llamar a la función sin proporcionar un valor.
greet_three()





