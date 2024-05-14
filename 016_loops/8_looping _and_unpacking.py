'''
Si deseas iterar sobre una lista de tuplas, por ejemplo:
'''

collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]

'''
En ves de hacer algo como esto: 
for item in collection:
    i1 = item[0]
    i2 = item[1]
    i3 = item[2]
# logic

o algo como esto

for item in collection:
    i1, i2, i3 = item

Se puede hacer algo como esto:
for i1, i2, i3 in collection:
    # Logica

'''

# Esto también funcionará para la mayoría de los tipos de iterables, no solo para tuplas

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



