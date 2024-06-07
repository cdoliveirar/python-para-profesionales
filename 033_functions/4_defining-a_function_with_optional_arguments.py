'''
Definir una función con argumentos opcionales
'''

''' Los argumentos opcionales pueden ser definidos asignando (usando = ) un valor por defecto al nombre del argumento.'''
def make(action='nothing'):
    return action

# Llamando esta funcion es posible en 3 diferentes maneras.
print(make("fun"))      # fun

print(make(action="sleep"))     # sleep

# El argumento es opcional, por lo que la función usará el valor predeterminado si el argumento no se proporciona.
print(make())       # nothing


'''
Advertencia
Los tipos mutables (lista, diccionario, conjunto, etc.) deben ser tratados con cuidado cuando se utilizan como 
atributos predeterminados. Cualquier mutación del argumento predeterminado cambiará permanentemente su valor. 
Consulta 'Definir una función con argumentos mutables opcionales' que es la siguiente seccion."
'''

print(make.__defaults__)