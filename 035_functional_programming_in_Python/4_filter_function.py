'''
Función Filter
'''

''' Filter toma una función y una colección. Devuelve una colección de cada elemento para el cual la función devuelve 
True.'''

arr=[1,2,3,4,5,6]
print([i for i in filter(lambda x:x>4,arr)])        # [5, 6]