'''
Definir una función con múltiples argumentos
'''

''' Uno puede dar a una función tantos argumentos como desee, las únicas reglas fijas son que cada nombre de argumento 
debe ser único y que los argumentos opcionales deben estar después de los que no son opcionales: '''

def func(valor1, valor2, valor_opcional=10):
    return '{0} {1} {2}'.format(valor1, valor2, valor_opcional)

''' Al llamar a la función puedes dar cada palabra clave sin el nombre, pero entonces el orden importa: '''
print(func(1, 'a', 100))        # 1 a 100
print(func('abc', 14))                      # abc 14 10



''' O combinar dando los argumentos con nombre y sin él. Luego, los que tienen nombre deben seguir a los que no tienen,
pero el orden de los que tienen nombre no importa: '''

print(func('Esto', valor2='es', valor_opcional='Documentación de StackOverflow'))
# Esto es Documentación de StackOverflow
