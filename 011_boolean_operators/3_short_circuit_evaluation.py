'''
https://en.wikipedia.org/wiki/Short-circuit_evaluation
'''


def short_circuit_evaluation():
    pass

def true_func():
    print("true_func()")
    return True

def false_func():
    print("false_func()")
    return False




if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    short_circuit_evaluation()
    print(true_func() or false_func())      # True
    print(false_func()  or true_func())     # True

    print(true_func() and false_func())     # False
    print(false_func() and false_func())    # False

