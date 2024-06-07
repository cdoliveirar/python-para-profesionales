'''
Elevar a la potencia
'''

'''
Parametros              detalles
X                       El número a ser elevado
y                       El exponente
raise                   La función a ser especializada
'''
'''
si vienes de la escuela de programación orientada a objetos (OOP), especializar una clase abstracta y usarla es una 
práctica que debes tener en cuenta al escribir tu código. 

¿Qué pasaría si pudieras definir una función abstracta y especializarla para crear diferentes versiones de ella? 
Piensa en ello como una especie de herencia de funciones donde vinculas parámetros específicos para hacerlas 
fiables en un escenario específico.
'''

''' Supongamos que queremos elevar x a un número y'''
def raise_power(x, y):
    return x**y

''' ¿Qué pasa si tu valor de y puede asumir un conjunto finito de valores?'''

'''
Supongamos que y puede ser uno de [3, 4, 5] y digamos que no quieres ofrecer al usuario final la posibilidad de usar 
dicha función ya que es muy intensiva en términos computacionales. De hecho, verificarías si el valor proporcionado 
de y es válido y reescribirías tu función como:
'''
def raise(x, y):
    if y in (3,4,5):
        return x**y
    raise NumberNotInRangeException("You should provide a valid exponent")

''' ¿Desordenado? Usemos la forma abstracta y especialicémosla para los tres casos: implementémoslos parcialmente'''

from functors import partial
raise_to_three = partial(raise, y=3)
raise_to_four = partial(raise, y=4)
raise_to_five = partial(raise, y=5)

'''
¿Qué pasa aquí? Fijamos los parámetros y y definimos tres funciones diferentes. No es necesario usar la función 
abstracta definida anteriormente (podrías hacerla privada), pero podrías usar funciones aplicadas parcialmente para 
tratar con la elevación de un número a un valor fijo.
'''



