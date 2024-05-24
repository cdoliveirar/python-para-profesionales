'''
La comprensión de conjuntos es similar a la comprensión de listas y de diccionarios, pero produce un set, que es
una colección desordenada de elementos únicos.
'''


# Un conjunto que contiene cada valor en el rango(5)
print({x for x in range(5)})    # {0, 1, 2, 3, 4}

# Un conjunto de números pares entre 1 y 10:
print({x for x in range(1, 11) if x % 2 == 0})      # {2, 4, 6, 8, 10}

# Caracteres alfabéticos únicos en una cadena de texto:
text = "When in the Course of human events it becomes necessary for one people..."
print({ch.lower() for ch in text if ch.isalpha()})
#  {'u', 'i', 'l', 'h', 'w', 't', 'y', 's', 'a', 'c', 'f', 'v', 'n', 'p', 'r', 'b', 'o', 'm', 'e'}

''' usando set buil-in '''
print(set(x for x in range(5)))     # {0, 1, 2, 3, 4}


