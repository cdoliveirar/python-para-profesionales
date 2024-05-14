'''
Las sentencias compuestas (bucles) for y while pueden opcionalmente tener una cláusula else (en la práctica,
este uso es bastante raro).

La cláusula else solo se ejecuta después de que un bucle for termina al iterar completamente, o después de que un
bucle while termina porque su expresión condicional se vuelve falsa.
'''
for i in range(3):
    print(i)
else:
    print('done')

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')


'''
La cláusula else no se ejecuta si el bucle termina de alguna otra manera (a través de una instrucción break o al 
lanzar una excepción).
'''
for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print('done')

'''
La mayoría de los otros lenguajes de programación carecen de esta cláusula else opcional en los bucles. El uso de la 
palabra clave else en particular a menudo se considera confuso.
El concepto original de dicha cláusula se remonta a Donald Knuth y el significado de la palabra clave else se aclara 
si reescribimos un bucle en términos de instrucciones if y goto de días anteriores antes de la programación 
estructurada o de un lenguaje de ensamblador de nivel inferior

Ejemplo 1:
    while loop_condition():
        ...
        if break_condition():
        break
        ...

Es equivalente a
# pseudocodigo

<<start>>:
if loop_condition():
    ...
    if break_condition():
        goto <<end>>
    ...
    goto <<start>>
<<end>>:


Estos siguen siendo equivalentes si les adjuntamos una cláusula else a cada uno de ellos

Ejemplo 2:
while loop_condition():
    ...
    if break_condition():
        break
    ...
else:
print('done')

Es equivalente a:
# pseudocodigo
<<start>>:
if loop_condition():
    ...
    if break_condition():
        goto <<end>>
    ...
    goto <<start>>
else:
    print('done')
<<end>>:

------------
------
Un bucle for con una cláusula else puede entenderse de la misma manera. Conceptualmente, hay una condición de bucle 
que permanece Verdadera mientras el objeto iterable o la secuencia todavía tengan algunos elementos restantes
'''

# ¿Por qué alguien usaría esta construcción extraña?
# El caso de uso principal para la construcción for...else es una implementación concisa de búsqueda,
a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")

# Para hacer que el else en esta construcción sea menos confuso, se puede pensar en él como "if not break" o
# "if not found".


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



