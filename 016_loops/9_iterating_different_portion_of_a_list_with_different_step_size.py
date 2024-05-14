'''
Supongamos que tienes una larga lista de elementos y solo estás interesado en cada otro elemento de la lista.
Tal vez solo quieras examinar los primeros o últimos elementos, o un rango específico de entradas en tu lista.
Python tiene fuertes capacidades integradas de indexación. Aquí tienes algunos ejemplos de cómo lograr estos escenarios
'''

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

# Iteración sobre toda la lista
# Para iterar sobre cada elemento en la lista, se puede usar un bucle for como el siguiente

for s in lst:
    print(s[:1]) # print the first letter

'''
A menudo necesitas tanto el elemento como el índice de ese elemento. La palabra clave enumerate realiza esa tarea.
'''
for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))

# Iterar sobre una sublista
# Si queremos iterar sobre un rango (recordando que Python utiliza indexación basada en cero), usamos la palabra
# clave range
for i in range(2,4):
    print("lst at %d contains %s" % (i, lst[i]))

'''
La lista también puede ser cortada. La siguiente notación de corte va desde el elemento en el índice 1 hasta el 
final con un paso de 2. Los dos bucles for dan el mismo resultado.
'''
for s in lst[1::2]:
    print(s)



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



