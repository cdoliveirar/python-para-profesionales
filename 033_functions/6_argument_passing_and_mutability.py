'''
Paso de argumentos y mutabilidad
'''

''' Primero, algo de terminología:
- argumento (parámetro actual): la variable real que se pasa a una función;
- parámetro (parámetro formal): la variable receptora que se usa en una función.

En Python, los argumentos se pasan por asignación (a diferencia de otros lenguajes, donde los argumentos pueden pasarse 
por valor/referencia/puntero).
'''

'''
- Mutar un parámetro mutará el argumento (si el tipo del argumento es mutable).
'''

def foo(x):         # aqui x es el parámetro
    x[0] = 9        # Esto muta la lista etiquetada tanto por x como por y.
    print(x)

y = [4, 5, 6]
foo(y)              # llama a foo con y como argumento

print(y)            # [9, 5, 6], lista etiquetada por y también ha sido mutada

'''
- Reasignar el parámetro no reasignará el argumento.
'''

def foo(x):             # aquí x es el parámetro, cuando llamamos a foo(y) asignamos y a x
    x[0] = 9            # esto muta la lista etiquetada tanto por x como por y
    x = [1, 2, 3]       # x ahora está etiquetando una lista diferente (y no se ve afectado)
    x[2] = 8            # esto muta la lista de x, no la lista de y

y = [4, 5, 6]           # y es el argumento, x es el parámetro
foo(y)                  # Supongamos que escribimos "x = y", luego ve a la línea 1
print(y)    # [9, 5, 6]
''' Entonces, cuando se imprime y después de llamar a la función foo, se imprimirá [9, 5, 6], ya que solo se modificó 
la lista original y en el primer paso de la función foo.
'''

''' En Python, en realidad no asignamos valores a las variables, en su lugar, vinculamos (es decir, asignamos, 
adjuntamos) variables (consideradas como nombres) a objetos.

- Inmutable: Enteros, cadenas, tuplas, y así sucesivamente. Todas las operaciones hacen copias.

- Mutables:Listas, diccionarios, set, y así sucesivamente. Las operaciones pueden o no mutar.
'''

x = [3, 1, 9]
y = x
x.append(5)         # Muta la lista etiquetada por x e y, ambos x e y están vinculados a [3, 1, 9]
x.sort()            # Muta la lista etiquetada por x e y (ordenación in situ)
x = x + [4]         # No muta la lista (hace una copia solo para x, no para y)
z = x               # z es x ([1, 3, 9, 4])
x += [6]            # Muta la lista etiquetada por x y z (utiliza la función extend).
x = sorted(x)       # No muta la lista (hace una copia solo para x).

print(x)    # [1, 3, 4, 5, 6, 9]
print(y)    # [1, 3, 5, 9]
print(z)    # [1, 3, 5, 9, 4, 6]




