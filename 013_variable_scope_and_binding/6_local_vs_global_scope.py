'''
¿Cuál es el ámbito local y global?
Todas las variables de Python que son accesibles en algún punto del código están o bien en el ámbito local o en el
ámbito global. La explicación es que el ámbito local incluye todas las variables definidas en la función actual y el
ámbito global incluye variables definidas fuera de la función actual.
'''

foo = 1                 # global
def func1():
    bar = 2             # local
    print(foo)          # prints variable foo from global scope
    print(bar)          # prints variable bar from local scope


'''
Se puede inspeccionar qué variables están en qué ámbito. Las funciones integradas locals() y globals() devuelven 
los ámbitos completos como diccionarios.
'''
foo = 1
def func2():
    bar = 2
    print(globals().keys())         # prints all variable names in global scope
    print(locals().keys())          # prints all variable names in local scope


'''
¿Qué sucede con los conflictos de nombres?
'''
foo = 1
def func3():
    foo = 2                         # creates a new variable foo in local scope, global foo is not affected
    print(foo)                      # prints 2
    # global variable foo still exists, unchanged:
    print(globals()['foo'])         # prints 1
    print(locals()['foo'])          # prints 2


'''
Para modificar la variable global, use la palabra clave global,
'''
foo = 1
def func4():
    global foo
    foo = 2                 # this modifies the global foo, rather than creating a local variable
    print(foo)              # print 2


# IMPORTANTE
# ----------
'''
El ámbito está definido para todo el cuerpo de la función!!
Lo que significa es que una variable nunca será global para la mitad de la función y local después, o viceversa.
'''
foo = 1
def func5():
    # This function has a local variable foo, because it is defined down below.
    # So, foo is local from this point. Global foo is hidden.
#    print(foo)          # raises UnboundLocalError, because local foo is not yet initialized
    foo = 7
    print(foo)

'''
Del mismo modo, lo contrario:
'''
foo = 1
def func6():
    # In this function, foo is a global variable from the beginning

    foo = 7                     # global foo is modified, solo es modificado para este scope
    print(foo)                  # 7
    print(globals()['foo'])     # 7
    #global foo                  # this could be anywhere within the function
    print(foo)                  # 7



#   Funciones dentro de funciones
'''
Puede haber muchos niveles de funciones anidadas dentro de funciones, pero dentro de cualquier función solo hay un 
ámbito local para esa función y el ámbito global. No hay ámbitos intermedios.
'''
foo = 1

def f1():
    bar = 1

    def f2():
        baz = 2
        # here, foo is a global variable, baz is a local variable
        # bar is not in either scope
        print(locals().keys())          # ['baz']
        print('bar' in locals())        # False
        print('bar' in globals())       # False

    def f3():
        baz = 3
        print(bar)          # bar from f1 is referenced so it enters local scope of f3 (closure)
        print(locals().keys())          # ['bar', 'baz']
        print('bar' in locals())        # True
        print('bar' in globals())       # False

    def f4():
        bar = 4             # a new local bar which hides bar from local scope of f1
        baz = 4
        print(bar)
        print(locals().keys())          # ['bar', 'baz']
        print('bar' in locals())        # True
        print('bar' in globals())       # False

    f2()
    f3()
    f4()


'''
global vs nonlocal (solo en Python 3)
Ambas palabras clave se utilizan para obtener acceso de escritura a variables que no son locales a las funciones 
actuales. La palabra clave global declara que un nombre debe tratarse como una variable global
'''
foo1 = 0         # global foo
def f11():
    print("global vs nonlocal")
    foo1 = 1                     # a new foo local in f1
    def f22():
        foo1 = 2                 # a new foo local in f2
        def f33():
            foo1 = 3             # a new foo local in f3
            print(foo1)          # 3
            foo = 30            # modifies local foo in f3 only
        def f44 ():
            global foo1
            print("f44")
            print(foo1)          # 0
            foo1 = 100           # modifies global foo
        f33()
        f44()
    f22()


'''
Por otro lado, nonlocal (ver Variables nonlocales), disponible en Python 3, toma una variable local de un ámbito 
circundante y la introduce en el ámbito local de la función actual.

La declaración nonlocal hace que los identificadores listados se refieran a variables previamente ligadas en el 
ámbito más cercano excluyendo las variables globales.
'''

def f1_1():
    def f2_2():
        foo = 2                 # a new foo local in f2_2

        def f3_3():
            nonlocal foo        # foo from f2_2, which is the nearest enclosing scope
            print(foo)          # 2
            foo = 200            # modifies foo from f2_2!
        f3_3()
        print(foo)
    f2_2()


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    func1()
    func2()
    func3()
    func4()
    func5()
    func6()
    print("Funciones dentro de funciones")
    f1()
    f11()
    f1_1()



