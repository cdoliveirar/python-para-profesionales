'''
Funciones anidadas
'''

''' Las funciones en Python son objetos de primera clase. Pueden ser definidas en cualquier ámbito.'''

def fibonacci(n):
    def step(a,b):
        return b, a+b
    a, b = 0, 1
    for i in range(n):
        a, b = step(a, b)
    return a

print(fibonacci(3))


''' Las funciones capturan su alcance envolvente y pueden ser pasadas alrededor como cualquier otro tipo de objeto'''
def make_adder(n):
    def adder(x):
        return n + x
    return adder
add5 = make_adder(5)
add6 = make_adder(6)
print(add5(10))     # 15
print(add6(10))     # 16


def repeatedly_apply(func, n, x):
    for i in range(n):
        x = func(x)
    return x

print(repeatedly_apply(add5, 5, 1))     # 26

