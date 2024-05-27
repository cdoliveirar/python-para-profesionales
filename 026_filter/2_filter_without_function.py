'''
Filtro sin funcion

Si el parámetro de la función es None, entonces se usará la función identidad.
'''

print(list(filter(None, [1, 0, 2, [], '', 'a'])))           # [1, 2, 'a']

''' cuando filter se usa con None, filtra los elementos del iterable que son True en un contexto booleano. 
En Python, los valores considerados como False incluyen 0, None, listas vacías [], cadenas vacías '', entre otros.

1 es True
0 es False
2 es True
[] es False
'' es False
'a' es True
'''

# Equivalente en comprension de listas
[i for i in [1, 0, 2, [], '', 'a'] if i]


# equivalenente en generador de expresiones
(i for i in [1, 0, 2, [], '', 'a'] if i)







import sys
generador = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(generador))

lista = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(lista))

