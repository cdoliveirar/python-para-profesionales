'''
Cierres
'''

''' Los cierres en Python se crean mediante llamadas a funciones. Aquí, la llamada a makeInc crea un enlace para x que 
es referenciado dentro de la función inc. Cada llamada a makeInc crea una nueva instancia de esta función, pero cada 
instancia tiene un enlace a un enlace diferente de x.'''

def makeInc(x):
    def inc(y):
        return x + y
    return inc


incOne = makeInc(1)
incFive = makeInc(5)

print(incOne(1))
print(incFive(5))

''' Observa que mientras que en un cierre regular la función encapsulada hereda completamente todas las variables de su 
entorno de cierre, en esta construcción la función encapsulada solo tiene acceso de lectura a las variables heredadas 
pero no puede hacer asignaciones a ellas.'''

def makeInc(x):
    def inc(y):
        nonlocal x
        # Ahora assinar un valor a x esta permitido
        x += y
        return x
    return inc

incOne = makeInc(1)
print(incOne(5))        # 6


''' clousure con multiplicacion'''
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

# Creamos instancias de la función multiplier con diferentes valores de x
multiply_by_2 = multiplier(2)
multiply_by_5 = multiplier(5)

# Usamos las funciones creadas para realizar multiplicaciones
print(multiply_by_2(3))  # Salida: 6 (2 * 3)
print(multiply_by_5(4))  # Salida: 20 (5 * 4)
