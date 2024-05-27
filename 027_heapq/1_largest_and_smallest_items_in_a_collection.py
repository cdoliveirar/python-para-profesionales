'''
Elementos más grandes y más pequeños en una colección

Para encontrar los elementos más grandes en una colección, el módulo heapq tiene una función llamada nlargest.
Le pasamos dos argumentos: el primero es el número de elementos que queremos recuperar, el segundo es el nombre de
la colección.
'''

import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers))           # [200, 150, 100, 50]

''' De manera similar, para encontrar los elementos más pequeños en una colección, usamos la función nsmallest.'''
print(heapq.nsmallest(4, numbers))          # [1, 2, 4, 8]


''' Tanto las funciones nlargest como nsmallest aceptan un argumento opcional (el parámetro key) para estructuras de 
datos complejas. El siguiente ejemplo muestra el uso de la propiedad age para recuperar a las personas más ancianas y 
más jóvenes del diccionario people:  '''

people = [
{'firstname': 'John', 'lastname': 'Doe', 'age': 30},
{'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
{'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
{'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
{'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
{'firstname': 'John', 'lastname': 'Roe', 'age': 45}
]

oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(oldest)
# [{'firstname': 'John', 'lastname': 'Roe', 'age': 45}, {'firstname': 'John', 'lastname': 'Doe', 'age': 30}]

youngest = heapq.nsmallest(2, people, key=lambda s: s['age'])
print(youngest)
# [{'firstname': 'Janie', 'lastname': 'Doe', 'age': 10}, {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12}]