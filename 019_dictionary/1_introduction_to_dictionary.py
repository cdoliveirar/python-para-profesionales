'''
Un diccionario es un ejemplo de un almacén de clave-valor, también conocido como Mapeo en Python. Permite
almacenar y recuperar elementos haciendo referencia a una clave. Dado que los diccionarios se referencian
por clave, tienen búsquedas muy rápidas. Como se utilizan principalmente para hacer referencia a elementos
por clave, no están ordenados.
'''

# Creando  diccionario(dict)
# Los diccionarios se pueden inicializar de muchas maneras.

# Sintaxis Literal
# ----------------
d = {}                  # diccionario vacio
d = {'key': 'value'}    # dict con valores iniciales

# Hace una copia superficial de otherdict.
d = {**otherdict}

# También actualiza la copia superficial con el contenido de yetanotherdict.
d = {**otherdict, **yetanotherdict}


# Comp0rensión de Diccionarios
# ---------------------------
d = {k:v for k,v in [('key', 'value',)]}

# Ver también: Comprensiones

# built-in class: dict()
# ----------------------
d = dict()                      # diccionario vacio
d = dict(key='value')           # argumentos de palabras clave explícitos
d = dict([('key', 'value')])    # pasar una lista de pares clave/valor
# hacer una copia superficial de otro diccionario (¡solo es posible si las claves son solo cadenas!)
d = dict(**otherdict)

'''
Modificar un diccionario
Para agregar elementos a un diccionario, simplemente crea una nueva clave con un valor.
'''
d['newkey'] = 42

# También es posible agregar listas y diccionarios como valores.
d['new_list'] = [1, 2, 3]
d['new_dict'] = {'nested_dict': 1}
