'''
Lambda recursivo usando variable asignada
'''
''' Un método para crear funciones lambda recursivas implica asignar la función a una variable y luego referenciar esa 
variable dentro de la función misma. Un ejemplo común de esto es el cálculo recursivo del factorial de un número, 
como se muestra en el siguiente código.'''

lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(4))  # 24

# Si i es igual a 0, la expresión devuelve 1, que es el caso base para el factorial.

# Si i no es igual a 0, la expresión devuelve i multiplicado por lambda_factorial(i-1). Esto es una llamada recursiva
# a la función lambda lambda_factorial, donde i-1 se pasa como argumento.

# La llamada recursiva continúa hasta que i se reduce a 0, momento en el que se alcanza el caso base y se devuelve 1
