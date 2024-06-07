'''
Devolver valores desde funciones
'''

''' Las funciones pueden devolver(return) un valor que puedes utilizar directamente'''
def give_me_five():
    return 5

print(give_me_five())   # imprime el valor devuelto

''' o guardar el valor para usarlo más tarde'''
num = give_me_five()
print(num)              # Imprime el valor devuelto guardado


''' o usar el valor para cualquier operación'''
print(give_me_five() + 10)      # 15


''' Si se encuentra un return en la función, la función se saldrá inmediatamente y las operaciones subsecuentes 
no serán evaluadas'''
def give_me_another_five():
    return 5
    print('Esta sentencia no será imprimida, más')

print(give_me_another_five())


''' También puedes devolver múltiples valores (en forma de una tupla).'''
def give_me_two_fives():
    return 5, 5 # devuelve dos 5

first, second = give_me_two_fives()
print(first)

print(second)

''' Una función sin declaración de retorno devuelve implícitamente None. De manera similar, una función con una 
declaración de retorno, pero sin valor de retorno o variable, devuelve None.'''