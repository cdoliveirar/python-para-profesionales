'''
Las tuplas son inmutables

Una de las principales diferencias entre listas y tuplas en Python es que las tuplas son inmutables, es decir, no se
pueden añadir o modificar elementos una vez que la tupla ha sido inicializada.
'''

t = (1, 4, 9)
# t[0] = 2            # TypeError: 'tuple' object does not support item assignment

''' De manera similar, las tuplas no tienen los métodos .append y .extend como las listas. Es posible usar +=, pero 
esto cambia la vinculación (binding) de la variable, y no la tupla en sí misma.'''

t = (1, 2)
q = t
t += (3, 4) # crea una nueva tupla que contiene los elementos de t y (3, 4), y reasigna esta nueva tupla a la variable t
print(t)
print(q)

''' Ten cuidado cuando coloques objetos mutables, como listas, dentro de tuplas. Esto puede llevar a resultados muy 
confusos cuando los cambies'''

t = (1, 2, 3, [1, 2, 3])
print(t)

try:
    t[3] += [4, 5]
except:
    print(t)
# he crearo un segmento try, se crea otra tupla t con (1, 2, 3, [1, 2, 3, 4, 5])

''' Puedes usar el operador += para "añadir" a una tupla - esto funciona creando una nueva tupla con el nuevo elemento 
que has "añadido" y asignándola a su variable actual; la tupla antigua no se modifica, ¡sino que es reemplazada!
Esto evita convertir de y hacia una lista, pero es lento y es una mala práctica, especialmente si vas a añadir 
múltiples veces.'''
