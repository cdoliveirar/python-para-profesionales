'''
Funciones y llamadas
'''

''' Las listas como argumentos son solo otra variable'''
def func(myList):
    for item in myList:
        print(item)

''' y se pueden pasar en la llamada a la función misma'''
func([1,2,3,5,7])

# 1
# 2
# 3
# 5
# 7

''' O como una variable'''
aList = ['a','b','c','d']
func(aList)

# a
# b
# c
# d
