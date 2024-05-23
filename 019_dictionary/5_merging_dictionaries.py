fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

fishdog = {**fish, **dog}
print(fishdog)      # {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}

'''
Como este ejemplo demuestra, las claves duplicadas se asignan a su valor más reciente (por ejemplo, "Clifford" 
reemplaza a "Nemo").
'''

from collections import ChainMap
print(dict(ChainMap(fish, dog)))  # {'name': 'Nemo', 'hands': 'fins', 'color': 'red', 'special': 'gills'}

# Con esta técnica, el valor principal tiene prioridad para una clave dada en lugar del último ("Clifford" se descarta
# a favor de "Nemo").


from itertools import chain
print(dict(chain(fish.items(), dog.items())))
#  {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}
# Esto utiliza el valor más reciente, al igual que la técnica basada en ** para fusionar ("Clifford" reemplaza a "Nemo").

fish.update(dog)
print(fish)
# dict.update utiliza el último diccionario para sobrescribir el anterior.
