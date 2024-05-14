def function_str_repr():
    # There are two functions that can be used to obtain a readable representation of an object.
    #repr()
    '''Para muchos tipos, esta función intenta devolver una cadena que generaría un objeto con el mismo valor.
    cuando se pasa a eval() . De lo contrario, la representación es una cadena encerrada entre corchetes angulares
    que contiene el nombre del tipo de objeto junto con información adicional. Esto suele incluir el nombre
    y la dirección del objeto.'''

    # str()
    '''Para cadenas, esto devuelve la cadena misma. La diferencia entre esto y repr(object) es que str(object) no
    No siempre intenta devolver una cadena que sea aceptable para eval() . Más bien, su objetivo es devolver 
    una imagen imprimible o "humana". cadena legible. Si no se proporciona ningún argumento, esto devuelve 
    la cadena vacía'''

    s = """w'o"w"""
    print(repr(s))  # Output: 'w\'o"w'
    print(str(s))  # Output: w'o"w
    # eval(str(s)) == s  # Gives a SyntaxError  # SyntaxError: EOL while scanning string literal
    eval(repr(s)) == s  # Output: True

    import datetime
    today = datetime.datetime.now()
    print(str(today))  # Output: '2016-09-15 06:58:46.915000'
    print(repr(today))  # Output: 'datetime.datetime(2016, 9, 15, 6, 58, 46, 915000)'

# When writing a class, you can override these methods to do whatever you want:
class Represent(object):

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)

    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)




# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_str_repr()

    # Usando la clase anterior podemos ver los resultados:
    r = Represent(1, "Hopper")
    print("-- Dentro de la clase --")
    print(r)  # prints __str__   # Representing x as 1 and y as Hopper
    print(r.__repr__)  # prints __repr__: '<bound method Represent.__repr__ of Represent(x=1,y="Hopper")>'
    rep = r.__repr__()  # sets the execution of __repr__ to a new variable
    print(rep)  # prints 'Represent(x=1,y="Hopper")'
    r2 = eval(rep)  # evaluates rep
    print(r2)  # prints __str__ from new object  # Representing x as 1 and y as Hopper
    print(r2 == r)  # prints 'False' because they are different objects