'''
Los diccionarios asignan claves a valores.
'''

car = {}
car["wheels"] = 4
car["color"] = "Red"
car["model"] = "Corvette"
print(car)

#  Los valores del diccionario pueden ser accedidos mediante sus claves.

print("Little " + car["color"] + " " + car["model"] + "!")

# Los diccionarios también pueden ser creados en un estilo JSON:
car = {"wheels": 4, "color": "Red", "model": "Corvette"}

for key in car:
    print(key + ": " + str(car[key]))