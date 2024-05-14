'''

'''


x = 'Hi'
def read_x():
    print(x)        # x is just referenced, therefore assumed global

read_x()            # prints Hi

y = 'Hallo'
def read_y():
    print(y)        # here y is just referenced, therefore assumed global

read_y()            #  prints Hallo

def read_y():
    y = 'Hey'
    print(y)


'''
Por lo general, una asignación dentro de un ámbito opacará cualquier variable externa del mismo nombre:
'''

x = 'Holas'
def change_local_x():
    x = 'Hola en Local'
    print(x)
change_local_x()    # prints Bye
print(x)            # prints Hi


'''
Declarar un nombre como global significa que, durante el resto del ámbito, cualquier asignación al nombre 
ocurrirá en el nivel superior del módulo
'''
x = 'variable global'
def change_global_x():
    global x
    x = 'Hola Local'
    print(x)


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    read_x()
    read_y()
    print("change_local_x: ")
    change_local_x()
    print("change_global_x: ")
    change_global_x()

