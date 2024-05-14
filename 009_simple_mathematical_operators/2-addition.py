import operator

'''

'''

def addition():
    a, b = 1, 2
    # Using the "+" operator:
    print(a+b)  # = 3
    print(operator.add(a, b))

    # El operador "+=" es equivalente a:
    print(operator.iadd(a, b))

    # Note: the + operator is also used for concatenating strings, lists and tuples:
    "first string " + "second string"   # = 'first string second string'
    [1, 2, 3] + [4, 5, 6]               # = [1, 2, 3, 4, 5, 6]




if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    addition()