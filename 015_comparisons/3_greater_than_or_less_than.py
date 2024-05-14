'''
x > y
x < y

Estos operadores comparan dos tipos de valores, son los operadores menor que y mayor que. Para números,
simplemente comparan los valores numéricos para ver cuál es mayor:
'''

print(12 > 4)       # True
print(12 < 4)       # False
print(1 < 4 )       # True

print("Cadenas")
'''
Para cadenas de texto, compararán lexicográficamente, lo que es similar al orden alfabético pero no es }
exactamente lo mismo.
'''
print("alpha" < "beta")     # True
print("gamma" > "beta")     # True
print("gamma" < "OMEGA")    # True


'''
En estas comparaciones, las letras minúsculas se consideran 'mayores que' las mayúsculas, por eso "gamma" < "OMEGA" 
es falso. Si todas fueran mayúsculas, devolvería el resultado esperado del orden alfabético
'''
print("GAMMA" < "OMEGA")


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


