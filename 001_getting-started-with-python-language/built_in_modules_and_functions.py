def function_built_in_modules_and_functions():
    print(pow(2, 3))

    # Para verificar la función incorporada en Python podemos usar dir(). Si se llama sin argumento, devuelve
    # los nombres en el alcance actual. De lo contrario, devolverá una lista alfabética de nombres que comprendan
    # (algunos de) el atributo del objeto dado, y de atributos alcanzables desde él.

    # Python se utiliza para obtener una lista de nombres de los elementos incorporados (built-ins)
    # disponibles en el entorno de Python. Los elementos incorporados son funciones y objetos que están
    # disponibles globalmente en todos los programas de Python sin necesidad de importar ningún módulo.

    print(dir(__builtins__))

    # To know the functionality of any function, we can use built in function help .
    help(max)

    # Built in modules contains extra functionalities. For example to get square root of a number we need to
    # include math module.
    import math
    print(math.sqrt(16))

    # To know all the functions in a module we can assign the functions list to a variable, and then print the variable.
    print(dir(math))

    # it seems __doc__ is useful to provide some documentation in, say, functions
    print(math.__doc__)
    # This module provides access to the mathematical functions
    # defined by the C standard.

    # Además de las funciones, también se puede proporcionar documentación en módulos
    # si creo el fichero: helloWorld.py
    import helloWorld
    print(helloWorld.__doc__)
    print(helloWorld.sayHello.__doc__)


# Para cualquier tipo definido por el usuario, sus atributos, los atributos de su clase y recursivamente los atributos de la base de su clase.
# las clases se pueden recuperar usando dir()
class MyClassObject(object):
    pass



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_built_in_modules_and_functions()
    print(dir(MyClassObject))