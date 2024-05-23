'''
Iterar sobre una lista

Python admite el uso de un bucle for directamente sobre una lista
'''

my_list = ['foo', 'bar', 'baz']
for item in my_list:
    print(item)

''' También puedes obtener la posición de cada elemento al mismo tiempo '''
for (index, item) in enumerate(my_list):
    print('The item in position {} is: {}'.format(index, item))

# The item in position 0 is: foo
# The item in position 1 is: bar
# The item in position 2 is: baz

''' La otra forma de iterar una lista basada en el valor del índice'''
for i in range(0,len(my_list)):
    print(my_list[i])

''' Tenga en cuenta que cambiar elementos en una lista mientras se itera sobre ella puede tener resultados i
nesperados '''
for item in my_list:
    if item == 'foo':
        del my_list[0]
    print(item)

# En este último ejemplo, eliminamos el primer elemento en la primera iteración, pero eso causó que se omitiera bar."

