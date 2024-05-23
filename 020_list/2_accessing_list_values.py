'''
Las listas de Python tienen índices que comienzan en cero y actúan como los arreglos en otros lenguajes de programación.
'''

lst = [1, 2, 3, 4]
print(lst)
print(lst[0])           # 1
print(lst[1])           # 2

''' Intentar acceder a un índice fuera de los límites de la lista provocará un error de IndexError.'''
# print(lst[4])         # IndexError: list index out of range

''' Los índices negativos se interpretan como contando desde el final de la lista. '''
print(lst[-1])          # 4
print(lst[-2])          # 3
# print(lst[-5])        # IndexError: list index out of range

# Esto es funcionalmente equivalente a
print(lst[len(lst)-1])  # 4

'''
Las listas permiten usar la notación de rebanadas (slices) como lst[start:end:step]. La salida de la notación de 
slice es una nueva lista que contiene elementos desde el índice de inicio hasta el fin-1. Si se omiten las opciones, 
inicio se establece por defecto al principio de la lista, fin al final de la lista y paso a 1.
'''
print("slicing:..")
print(lst[:])           # [1, 2, 3, 4], devuelve todos los elementos de la lista
print(lst[::])          # [1, 2, 3, 4], devuelve todos los elementos de la lista
print(lst[:3])          # [1, 2, 3], Devuelve los elementos desde el inicio de la lista hasta el índice 2
                        # (el índice 3 no se incluye).

print(lst[::2])         # [1, 3], Devuelve todos los elementos de la lista, tomando un elemento y saltando uno (es decir,
                        # con un paso de 2).

print(lst[::-1])        # [4, 3, 2, 1], Devuelve todos los elementos de la lista en orden inverso, debido a que el paso es -1.
print(lst[-1:0:-1])     # [4, 3, 2], Devuelve los elementos desde el último elemento hasta el primer elemento,
                        # pero sin incluir el primer elemento (índice 0).
                        # Comenzar desde el último elemento (lst[-1] que es 4)
                        # Continuar hasta el primer elemento (lst[0] que es 1), pero sin incluirlo.
                        # Recorrer la lista hacia atrás con un paso de -1.

print(lst[5:8])         # []    Dado que el índice de inicio es mayor que la longitud de la lista, devuelve una lista vacía.
print(lst[1:10])        # [2, 3, 4]

'''
Conceptos slicing
1 - start: el índice donde comienza el slice (inclusive). Si se omite, se asume que es el inicio de la lista (índice 0).

2 - stop: el índice donde termina el slice (exclusivo). Es decir, el elemento en el índice stop no se incluye en el 
resultado. Si se omite, se asume que es el final de la lista.

3 - step: el intervalo entre cada índice del slice. Si se omite, se asume que es 1. Puede ser negativo para indicar 
que se debe recorrer la lista hacia atrás.
'''

''' Con esto en mente, puedes imprimir una versión invertida de la lista llamando a'''
print(lst[::-1])        # [4, 3, 2, 1]

'''Cuando se utilizan pasos de longitud negativa, el índice de inicio debe ser mayor que el índice de finalización; 
de lo contrario, el resultado será una lista vacía.'''
print(lst[3:1:-1])      # [4, 3]

'''Usar índices de paso negativo es equivalente al siguiente código '''
# reversed(lst)[0:2] # revision py3



'''Slicing avanzado'''
'''
Cuando las listas son cortadas, se llama al método __getitem__() del objeto lista, con un objeto slice. Python tiene 
un método incorporado llamado slice para generar objetos slice. Podemos usar esto para almacenar un slice y 
reutilizarlo más tarde de la siguiente manera,
'''
data = 'chandan purohit    22 2000'        # suponiendo campos de datos de longitud fija
name_slice = slice(0,19)
age_slice = slice(19,21)
salary_slice = slice(22,None)

print(data[name_slice])         #chandan purohit
print(data[age_slice])          #'22'
print(data[salary_slice])       #'2000'

''' Esto puede ser de gran utilidad al proporcionar funcionalidad de slicing a nuestros objetos al sobrescribir 
__getitem__ en nuestra clase'''

