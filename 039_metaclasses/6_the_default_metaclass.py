'''
La metaclase por defecto
'''

''' Es posible que hayas escuchado que todo en Python es un objeto. Es cierto, y todos los objetos tienen una clase:'''
print(type(1))      # <class 'int'>

''' El literal 1 es una instancia de la clase int. Declaremos una clase '''
class Foo(object):
    pass

''' Ahora instanciémosla'''
bar = Foo()

''' ¿Cuál es la clase de bar?'''
print(type(bar))        # <class '__main__.Foo'>

''' Ok, Foo mismo es una instancia de type. ¿Y qué hay de type?'''
print(type(type))       # <class 'type'>

''' Entonces, ¿qué es una metaclase? Por ahora, finjamos que es solo un nombre elegante para la clase de una clase. 
Conclusiones:

* Todo es un objeto en Python, por lo que todo tiene una clase
* La clase de una clase se llama metaclase
* La metaclase por defecto es type, y con mucho, es la metaclase más común

Pero, ¿por qué deberías saber sobre las metaclases? Bueno, Python en sí es bastante "hackeable", y el concepto de 
metaclase es importante si estás haciendo cosas avanzadas como metaprogramación o si quieres controlar cómo se 
inicializan tus clases.'''
