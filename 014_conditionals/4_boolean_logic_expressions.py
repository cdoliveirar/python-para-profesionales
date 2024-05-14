'''
Las expresiones de lógica booleana, además de evaluar a Verdadero o Falso, devuelven el valor que fue interpretado
como Verdadero o Falso. Es una forma pythonica de representar la lógica que de otra manera requeriría
una prueba de if-else
'''


# And operator
'''
El operador 'and' evalúa todas las expresiones y devuelve la última expresión si todas las expresiones se evalúan 
como Verdadero. De lo contrario, devuelve el primer valor que se evalúa como Falso
'''
print(1 and 2)              # 2 , devuelve la última expresion...
print(1 and 0)              # 0 , devuelve la última expresion...
print(1 and "Hello World")  # Hello World , devuelve la última expresion...
print("" and "Pancakes")    # ""    , Empty sequences: "" , devuelve "" como False.


# Or operator
'''
El operador 'or' evalúa las expresiones de izquierda a derecha y devuelve el primer valor que se evalúa como 
Verdadero o el último valor (si ninguno es Verdadero).
'''
print(1 or 2)               # 1,     primer valor evaluado como verdadero
print(None or 1)            # 1,     primer valor evaluado como verdadero
print(0 or [])              # [],    devuelve segundo valor en este caso ambos son falsos
print(4 or ())              # 4,     primer valor evaluado como verdadero
print('' or 10)             # 10,    segundo valor evaluado como verdadero
print({} or True)           # True   segundo valor evaluado como verdadero
print({} or False)          # False  devuelve segundo valor en este caso ambos son falsos


# Lazy evaluation
'''
Cuando utilizas este enfoque, recuerda que la evaluación es perezosa. Las expresiones que no son necesarias para 
determinar el resultado no se evalúan. Por ejemplo
'''
def print_me():
    print('Estoy aquí!')

print(0 and print_me())     # 0
'''
En el ejemplo anterior, print_me nunca se ejecuta porque Python puede determinar que toda la expresión es Falsa 
cuando encuentra el 0 (Falso). Ten esto en cuenta si print_me necesita ejecutarse para servir a la lógica 
de tu programa.
'''

# Pruebas para multiple condiciones

# Un error común al verificar múltiples condiciones es aplicar la lógica incorrectamente.
'''
Este ejemplo intenta verificar si dos variables son cada una mayor que 2. La declaración se evalúa como 
- if (a) and (b > 2). Esto produce un resultado inesperado porque bool(a) se evalúa como Verdadero cuando a no es cero.
'''
a = 1
b = 6
if a and b > 2:
    print('yes')       # yes
else:
    print('no')

# Cada variable debe compararse por separado.
if a > 2 and b > 2:
    print('yes')
else:
    print('no')

'''
Otro error similar se comete al verificar si una variable es uno de varios valores. La declaración en este 
ejemplo se evalúa como - if (a == 3) or (4) or (6). Esto produce un resultado inesperado porque bool(4) y bool(6) 
cada uno se evalúa como True.
'''
a = 1
if a == 3 or 4 or 6:
    print('yes')
else:
    print('no')

# Nuevamente, cada comparación debe hacerse por separado.}

if a == 3 or a == 4 or a == 6:
    print('yes')
else:
    print('no')

# Usar el operador 'in' es la manera canónica de escribir esto.
if a in (3, 4, 6):
    print('yes')
else:
    print('no')




if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


