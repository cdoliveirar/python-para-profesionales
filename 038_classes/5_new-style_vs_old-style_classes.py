'''
Clases de estilo nuevo vs. clases de estilo antiguo
'''

''' Las clases de estilo nuevo en Python 3 heredan implícitamente de object, por lo que ya no es necesario especificar 
MyClass(object).'''

class MyClass:
    pass

my_inst = MyClass()
print(type(my_inst))                    # <class '__main__.MyClass'>
print(my_inst.__class__)                # <class '__main__.MyClass'>
print(issubclass(MyClass, object))      # True
