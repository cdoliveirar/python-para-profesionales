'''
Los bucles 'for' iteran sobre una colección de elementos, como una lista(list) o un diccionario(dict), y ejecutan un
bloque de código con cada elemento de la colección.
'''

for i in [0, 1, 2, 3, 4]:
    print(i)

'''
El bucle 'for' anterior itera sobre una lista de números. En cada iteración, establece el valor de 'i' en el 
siguiente elemento de la lista. Por lo tanto, primero será 0, luego 1, luego 2, etc.
'''

# range es una función que devuelve una serie de números en forma de iterable, por lo tanto, puede ser usada en bucles for.
print("Range")
for i in range(5):
    print(i)
'''
da el mismo resultado exacto que el primer bucle 'for'. Ten en cuenta que el 5 no se imprime, ya que el rango aquí 
son los primeros cinco números empezando desde 0
'''



'''
Objetos iterables e iteradores
------------------------------
El bucle 'for' puede iterar sobre cualquier objeto iterable, que es un objeto que define una función __getitem__ o una 
función __iter__.
La función __iter__ devuelve un iterador, que es un objeto con una función next que se utiliza para acceder al siguiente
elemento del iterable.
'''


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



