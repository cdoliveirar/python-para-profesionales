'''
Enumerando Todos los Miembros de una Clase
'''

''' La función dir() se puede utilizar para obtener una lista de los miembros de una clase:
dir(Clase) '''

print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']

''' Es común buscar solo los miembros que no son "mágicos". Esto se puede hacer utilizando una simple comprensión que 
enumera los miembros cuyos nombres no comienzan con __:'''

print([m for m in dir(list) if not m.startswith('__')])

# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


''' Advertencias:
Las clases pueden definir un método dir(). Si ese método existe, llamar a dir() llamará a dir(), de lo contrario, 
Python intentará crear una lista de miembros de la clase. Esto significa que la función dir puede tener resultados 
inesperados. Dos citas de importancia de la documentación oficial de Python:

* Si el objeto no proporciona dir(), la función hace todo lo posible para recopilar información del atributo dict del 
objeto, si está definido, y de su objeto tipo. La lista resultante no necesariamente es completa y puede ser inexacta 
cuando el objeto tiene un getattr() personalizado.

* Nota: Debido a que dir() se suministra principalmente como una conveniencia para su uso en un indicador interactivo, 
trata de suministrar un conjunto interesante de nombres más que tratar de suministrar un conjunto de nombres 
rigurosamente o consistentemente definido, y su comportamiento detallado puede cambiar entre versiones. Por ejemplo, 
los atributos de la metaclase no están en la lista de resultados cuando el argumento es una clase.

'''
