'''
Evita operaciones repetitivas y costosas usando una cláusula condicional
'''

def f(x):
    import time
    time.sleep(.1)      # Simular función costosa, Pausa de 0.1 segundos
    return x ** 2

print([f(x) for x in range(10) if f(x) > 10])


'''
Esto da como resultado dos llamadas a f(x) para 1,00 valores de x: una llamada para generar el valor y la otra para 
verificar la condición if. Si f(x) es una operación particularmente costosa, esto puede tener implicaciones 
significativas en el rendimiento. Peor aún, si llamar a f() tiene efectos secundarios, puede producir resultados 
sorprendentes.
'''

'''En su lugar, deberías evaluar la operación costosa solo una vez para cada valor de x generando un iterable 
intermedio (expresión generadora) de la siguiente manera:'''


print([v for v in (f(x) for x in range(10)) if v > 10])

''' Otra forma que podría resultar en un código más legible es poner el resultado parcial (v en el ejemplo anterior) 
en un iterable (como una lista o una tupla) y luego iterar sobre él. Dado que v será el único elemento en el iterable, 
el resultado es que ahora tenemos una referencia a la salida de nuestra función lenta, calculada solo una vez.'''

print([v for x in range(10) for v in [f(x)] if v > 10])


''' Sin embargo, en la práctica, la lógica del código puede ser más complicada y es importante mantenerla legible. 
En general, se recomienda una función generadora separada en lugar de una línea compleja.
def process_prime_numbers(iterable):
    for x in iterable:
        if is_prime(x):
            yield f(x)

[x for x in process_prime_numbers(range(1000)) if x > 10]


Otra forma de evitar calcular f(x) varias veces es usar el decorador @functools.lru_cache() (Python 3.2+) en f(x). 
De esta manera, dado que la salida de f para la entrada x ya ha sido calculada una vez, la segunda invocación de la 
función en la comprensión de listas original será tan rápida como una consulta a un diccionario. Este enfoque utiliza 
memoización para mejorar la eficiencia, lo cual es comparable a usar expresiones generadoras.
'''


# Supongamos que tienes que aplanar una lista
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

# Algunos de los metodos pordrian ser:
    # reduce(lambda x, y: x+y, l)
    # sum(l, [])
    # list(itertools.chain(*l))

''' Sin embargo, la comprensión de listas proporcionaría la mejor tiempo de  complejidad. '''


