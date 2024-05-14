'''
Para iterar a través de una lista puedes usar un for
'''

for x in ['one', 'two', 'three', 'four']:
    print(x)

# La función range genera números que también son frecuentemente utilizados en un bucle for
for x in range(1, 6):
    print(x)

'''
enumerate
---------
Si deseas recorrer tanto los elementos de una lista como tener un índice para los elementos también, puedes usar
la función enumerate de Python:
'''
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)
'''
Enumerate generará tuplas, las cuales son desempaquetadas en un índice (un entero) y un elemento 
(el valor real de la lista). 
El bucle anterior imprimirá

(0,'::','one')
(1,'::','two')
(2,'::','three')
(3,'::','four')
'''

'''
map  --- map(función, iterable)
Donde función es la función que se aplicará a cada elemento del iterable, y iterable es el iterable sobre el cual se aplicará la función
--- --- --- ---
Iterar sobre una lista con manipulación de valores usando map y lambda, es decir, aplica una función lambda a cada 
elemento de la lista
'''

x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(list(x))



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



