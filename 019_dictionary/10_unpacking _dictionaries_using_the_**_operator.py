'''
Puedes usar el operador de desempaquetado de argumentos de palabra clave ** para pasar los pares clave-valor de un
diccionario como argumentos de una función.
'''


def parrot(voltage, state, action):
    print("This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)

# Como demuestra este ejemplo, las claves duplicadas se asignan a su valor más reciente (por ejemplo, "Clifford"
# reemplaza a "Nemo").
