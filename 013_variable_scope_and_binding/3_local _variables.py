'''
Si un nombre está vinculado dentro de una función, por defecto solo es accesible dentro de la función
'''

def foo1():
    a = 5
    print(a)    # ok
#print(a)    # NameError: name 'a' is not defined

def foo2():
    if True:
        a = 5
    print(a) # ok

b = 3
def bar():
    if False:
        b = 5
    print(b)

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    foo1()
    foo2()
    bar()


