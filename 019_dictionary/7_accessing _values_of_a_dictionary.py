dictionary = {"Hello": 1234, "World": 5678}
print(dictionary["Hello"])      # 1234

'''
El número 1234 se ve después del respectivo dos puntos en la definición del diccionario. Esto se llama el valor
al que "Hello" está mapeado en este diccionario.
'''

'''
Buscar un valor de esta manera con una clave que no existe generará una excepción KeyError, deteniendo la ejecución 
si no se captura. Si queremos acceder a un valor sin arriesgarnos a un KeyError, podemos usar el método get del 
diccionario. Por defecto, si la clave no existe, el método devolverá None. Podemos pasarle un segundo valor para 
que lo devuelva en lugar de None en caso de una búsqueda fallida.

w = dictionary.get("whatever")
x = dictionary.get("whatever", "nuh-uh")

En este ejemplo, 
w obtendrá el valor None y 
x obtendrá el valor "nuh-uh". !!
'''
