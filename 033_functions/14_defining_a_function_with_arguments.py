'''
Definiendo una funcion conargumentos
'''

''' Los argumentos se definen entre paréntesis después del nombre de la función:'''

def dividir(dividendo, divisor):    # Los nombres de la función y sus argumentos
    # Los argumentos están disponibles por nombre en el cuerpo de la función
    print(dividendo / divisor)

''' El nombre de la función y su lista de argumentos se llaman la firma de la función. Cada argumento con nombre es 
efectivamente una variable local de la función.

Al llamar a la función, proporciona valores para los argumentos enumerándolos en orden:
'''

print(dividir(10, 2))



