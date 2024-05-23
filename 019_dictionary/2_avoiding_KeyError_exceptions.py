'''
Un error común al usar diccionarios es intentar acceder a una clave inexistente. Esto generalmente resulta en una
excepción KeyError.

mydict = {}
mydict['not there']   # KeyError: 'not_there', este error es devido estás intentando acceder a una clave que no existe
# en el diccionario
'''
'''
Una forma de evitar errores de clave (KeyError) es usar el método get() del diccionario, que te permite especificar un 
valor predeterminado para devolver en caso de que la clave esté ausente.

value = mydict.get(key, default_value)

Que devuelve mydict[key] si existe, pero en caso contrario devuelve default_value. Ten en cuenta que esto no añade 
la clave a mydict. Por lo tanto, si deseas conservar ese par clave-valor, 
debes usar mydict.setdefault(key, default_value), que sí almacena el par clave-valor.
'''

mydict = {}
print(mydict)                           # {}

print(mydict.get("foo", "bar"))         # bar, en este caso devuelve el default_value

print(mydict)                           # {}

print(mydict.setdefault("foo", "bar"))  # bar

print(mydict)                           # {'foo': 'bar'}

print(mydict.get('0','no existe el Key 0')) # no existe el Key 0

'''
Una forma alternativa de lidiar con el problema es capturar la excepción

try:
    value = mydict[key]
except KeyError:
    value = default_value

También podrías comprobar si la clave está en el diccionario.

if key in mydict:
    value = mydict[key]
else:
    value = default_value

Ten en cuenta, sin embargo, que en entornos de múltiples hilos es posible que la clave sea eliminada del diccionario 
después de que la compruebes, creando una condición de carrera donde la excepción aún puede ser lanzada.

Otra opción es usar una subclase de dict, collections.defaultdict, que tiene un default_factory para crear nuevas 
entradas en el diccionario cuando se le proporciona una nueva clave (new_key).

'''
