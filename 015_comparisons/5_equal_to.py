'''
x == y

Esta expresión evalúa si x e y tienen el mismo valor y devuelve el resultado como un valor booleano. Generalmente,
tanto el tipo como el valor deben coincidir, por lo que el entero 12 no es lo mismo que la cadena '12'.
'''

print(12 == 12)                 # True
print(12 == 1)                  # False
print('12' == '12')             # True
print('spam' == 'spam')         # True
print('spam' == 'spam ')        # False
print('12' == 12)               # False


'''
Ten en cuenta que cada tipo debe definir una función que se utilizará para evaluar si dos valores son iguales. 
Para los tipos integrados, estas funciones se comportan como esperarías y simplemente evalúan las cosas en función 
de ser el mismo valor. Sin embargo, los tipos personalizados podrían definir las pruebas de igualdad como prefieran, 
incluyendo devolver siempre True o siempre False.
'''




if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


