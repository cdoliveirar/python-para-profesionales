'''
Iterar sobre diccionarios
'''

d = {"a": 1, "b": 2, "c": 3}
# Para iterar a través de sus claves, puedes usar
for key in d:
    print(key, d[key])
    print(key)

# Para iterar a través de sus valores, usa
for value in d.values():
    print(value)


# Para iterar a través de sus claves y valores, usa
for key, value in d.items():
    print(key, "::", value)


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



