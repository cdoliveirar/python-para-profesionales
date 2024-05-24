'''
Contando ocurrencias usando comprensiones

Cuando queremos contar el número de elementos en un iterable que cumplen alguna condición, podemos usar comprensiones
para producir una sintaxis idiomática:
'''

# Contar los números en range(1000) que son pares y contienen el dígito 9:
print(sum(1 for x in range(1000)
        if x % 2 == 0 and
        '9' in str(x)
        ))              # 95

'''
El concepto básico se puede resumir de la siguiente manera:

1- Iterar sobre los elementos en range(1000).
2- Concatenar todas las condiciones if necesarias.
3- Usar 1 como expresión para devolver un 1 para cada elemento que cumpla las condiciones.
4  Sumar todos los 1 para determinar el número de elementos que cumplen las condiciones.

Nota: Aquí no estamos recolectando los 1 en una lista (nota la ausencia de corchetes), sino que pasamos los unos 
directamente a la función sum que los suma. Esto se llama una expresión generadora, que es similar a una comprensión.

'''