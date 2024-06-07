'''
Funciones Recursivas
'''

''' Una función recursiva es una función que se llama a sí misma en su definición. Por ejemplo, la función matemática 
factorial, definida por factorial(n) = n*(n-1)(n-2)...3*2*1, puede ser programada como:'''

def factorial(n):
    #n here should be an integer
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(0)) # 1
print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(3)) # 6


''' Como se esperaba. Observa que esta función es recursiva porque el segundo retorno, factorial(n-1), donde la función 
se llama a sí misma en su definición.
Algunas funciones recursivas pueden ser implementadas usando lambda, la función factorial usando lambda sería algo 
así:'''

factorial = lambda n: 1 if n == 0 else n*factorial(n-1)

''' La función produce la misma salida que la anterior.'''

