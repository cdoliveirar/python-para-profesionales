'''
Crear una clase singleton con un decorador.
'''

''' Un singleton es un patrón que restringe la instanciación de una clase a una única instancia/objeto. Usando un 
decorador, podemos definir una clase como un singleton al forzar a la clase a devolver una instancia existente de la 
clase o crear una nueva instancia (si no existe).'''

def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper

''' Este decorador se puede agregar a cualquier declaración de clase y se asegurará de que como máximo se cree una 
instancia de la clase. Cualquier llamada subsiguiente devolverá la instancia de clase ya existente.'''

@singleton
class SomeSingletonClass:
    x = 2
    def __init__(self):
        print("Created!")

instance = SomeSingletonClass()     # Created!
instance = SomeSingletonClass()     # no se imprime nada

print(instance.x)

print(SomeSingletonClass().x)

''' Así que no importa si te refieres a la instancia de clase a través de tu variable local o si creas otra 
"instancia", siempre obtendrás el mismo objeto.'''


''' Explicaccion del instance[0]
La variable instance es una lista simple que contiene un solo elemento en la posición 0. Este único elemento es 
utilizado para almacenar la instancia de la clase cls. Cuando se llama a la función wrapper, se comprueba si esta 
posición contiene None, lo que indica que aún no se ha creado ninguna instancia de la clase. Si es así, se crea una 
nueva instancia y se asigna a esa posición de la lista. En las llamadas posteriores a wrapper, simplemente se devuelve 
la instancia almacenada en esa posición de la lista en lugar de crear una nueva instancia cada vez.


'''