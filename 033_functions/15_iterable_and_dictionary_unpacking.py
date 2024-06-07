'''
Desempaquetado de iterables y diccionarios
'''

''' Las funciones te permiten especificar estos tipos de parámetros: posicionales, nombrados, posicionales variables, 
Argumentos de palabras clave (kwargs). Aquí tienes un uso claro y conciso de cada tipo.'''

def unpacking(a, b, c=45, d=60, *args, **kwargs):
    print(a, b, c, d, args, kwargs)

unpacking(1, 2)                  # 1 2 45 60 () {}

unpacking(1, 2, 3, 4)       # 1 2 3 4 () {}
unpacking(1, 2, c=3, d=4)           # 1 2 3 4 () {}
unpacking(1, 2, d=4, c=3)           # 1 2 3 4 () {}

pair = (3,)
unpacking(1, 2,*pair, d=4)     # 1 2 3 4 () {}
unpacking(1, 2, d=4, *pair)     # 1 2 3 4 () {}

# unpacking(1, 2, *pair, c=3)     # TypeError: unpacking() got multiple values for argument 'c'


args_list = [3]
unpacking(1, 2, *args_list, d=4)    # 1 2 3 4 () {}
unpacking(1, 2, d=4, *args_list)    # 1 2 3 4 () {}

# unpacking(1, 2, c=3, *args_list)  # TypeError: unpacking() got multiple values for argument 'c'


pair = (3, 4)
unpacking(1, 2, *pair)                  # 1 2 3 4 () {}
unpacking(1, 2, 3, 4, *pair)        # 1 2 3 4 (3, 4) {}
# unpacking(1, 2, d=4, *pair)     # TypeError: unpacking() got multiple values for argument 'd'
# unpacking(1, 2, *pair, d=4) # TypeError: unpacking() got multiple values for argument 'd'

args_list = [3, 4]
unpacking(1, 2, *args_list)     # 1 2 3 4 () {}
unpacking(1, 2, 3, 4, *args_list)       # 1 2 3 4 (3, 4) {}
# unpacking(1, 2, d=4, *args_list)        # unpacking() got multiple values for argument 'd'
# unpacking(1, 2, *args_list, d=4)    # unpacking() got multiple values for argument 'd'

arg_dict = {'c':3, 'd':4}
unpacking(1, 2, **arg_dict)     # 1 2 3 4 () {}

arg_dict = {'d':4, 'c':3}
unpacking(1, 2, **arg_dict)     # 1 2 3 4 () {}

arg_dict = {'c':3, 'd':4, 'not_a_parameter': 75}
unpacking(1, 2, **arg_dict)         # 1 2 3 4 () {'not_a_parameter': 75}


# unpacking(1, 2, *pair, **arg_dict)       # TypeError: unpacking() got multiple values for argument 'c'
# unpacking(1, 2, 3, 4, **arg_dict)   # TypeError: unpacking() got multiple values for argument 'c'

# unpacking(1, 2, **arg_dict, c=3)  # TypeError: __main__.unpacking() got multiple values for keyword argument 'c'