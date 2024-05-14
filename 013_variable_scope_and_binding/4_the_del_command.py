'''
Este comando tiene varias formas relacionadas pero distintas
'''

def del_command():
    '''
    Si v es una variable, el comando del v elimina la variable de su scope
    '''
    x = 5
    print(x)    # out: 5
    del x
    #print(x)    # NameError: name 'f' is not defined



'''
del v.name
This command triggers a call to v.__delattr__(name) .
La intención es hacer que el atributo name no esté disponible
'''

class A:
    pass

a = A()
a.x = 7
print(a.x)      # out: 7
del a.x
# print(a.x)      # error: AttributeError: 'A' object has no attribute 'x'



'''
del v[item]
This command triggers a call to v.__delitem__(item)
La intención es que el elemento no pertenezca al mapeo implementado por el objeto v
'''
x = {'a': 1, 'b': 2}
print(x)
del x['a']          # out: {'b': 2}
print(x)
# print(x['a'])       # error: KeyError: 'a'

'''
del v[a:b]
Esto  llama a v.delslice(a, b)
La intención es similar a la descrita anteriormente, pero con slices, es decir, rangos de elementos en lugar 
de un solo elemento.
'''
x = [0, 1, 2, 3, 4]
del x[1:3]
print(x)            # out: [0, 3, 4]


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    del_command()


