'''
La palabra reservada "nonlocal" en Python se utiliza dentro de una función anidada para indicar que una variable
definida en un ámbito externo al de la función anidada debe ser modificada. Esto permite que la función anidada
acceda y modifique variables en el ámbito de una función que la contiene, pero que no es la
función inmediatamente contenedora.
'''
def no_local_variable():
    pass

def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

'''
Se debe usar nonlocal en funciones anidadas!!.
'''

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    no_local_variable()
    contador = counter()
    print(contador())