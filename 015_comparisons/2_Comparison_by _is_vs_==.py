'''
Un error común es confundir los operadores de comparación de igualdad "is" y "==".

"a == b" compara el valor de "a"

"a is b" compara las identidades de "a" y "b".
'''

a = 'Python is divertido!'
b = 'Python is divertido!'
print(a == b)       # devuelve True
print(a is b)       # a is b también podría dar True, pero no está garantizado.

a = [1, 2, 3, 4, 5]         # Creamos una lista a con cinco elementos.
b = a               # b references a, a y b ahora hacen referencia a la misma lista en memoria.
print(a == b)       # True, a y b hacen referencia a la misma lista y, por lo tanto, tienen los mismos elementos.
print(a is b)       # True,  porque a y b hacen referencia al mismo objeto en memoria, es decir, son el mismo objeto.

b = a[:]            # b now references a copy of a, Aquí estamos creando una copia superficial (shallow copy) de la
                    # lista a y haciendo que b apunte a esa copia. Una copia superficial crea una nueva lista, pero
                    # los elementos de la nueva lista son referencias a los mismos objetos que están en la lista original.
print(a == b)       # True, porque la nueva lista a la que b apunta es una copia exacta de la lista original a,
                    # con los mismos elementos.

print(a is b)       # False [!!], Aquí es donde surge la diferencia. Aunque los elementos de a y b son los mismos,
                    # a y b ya no apuntan al mismo objeto en memoria. a todavía apunta a la lista original, mientras
                    # que b apunta a una copia de esa lista. Por lo tanto, a is b devuelve False porque a y b son
                    # objetos diferentes en memoria.

'''
Básicamente, se puede pensar en "is" como una forma abreviada de id(a) == id(b).

Más allá de esto, hay particularidades del entorno de ejecución que complican aún más las cosas. Las cadenas cortas 
y los enteros pequeños devolverán True al ser comparados con is, debido a que la máquina de Python intenta utilizar 
menos memoria para objetos idénticos!!.
'''

a = 'short'
b = 'short'
c = 5
d = 5
print(a is b)
print(c is d)

# Pero las cadenas más largas y los enteros más grandes serán almacenados por separado.
a = 'Una cadena que no sea muy corta'
b = 'Una cadena que no sea muy corta'
c = 10000
d = 10000
print(a is b)
print(c is d)

# !!!
# Deberías usar is para verificar None:
if myvar is not None:
    # not None
    pass
if myvar is None:
    # None
    pass

# Un uso de is es para probar un "centinela" (es decir, un objeto único).
sentinel = object()
def myfunc(var=sentinel):
    if var is sentinel:
        # value wasn’t provided
        pass
    else:
        # value was provided
        pass


'''
sentinel se utiliza como un objeto único, que actúa como un marcador para indicar si se ha proporcionado un valor 
para var o no. La función myfunc puede aceptar un argumento opcional var, y si el valor predeterminado sentinel 
se pasa a var, entonces sabemos que ningún valor fue proporcionado explícitamente al llamar a la función.

Este enfoque se usa a menudo para distinguir entre valores predeterminados y valores proporcionados por el usuario. 
En este caso, sentinel se utiliza como una señal específica para indicar que no se proporcionó ningún valor.
'''


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



