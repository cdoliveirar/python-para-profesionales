'''
Puedes usar la función reversed, que devuelve un iterador a la lista invertida.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

rev = reversed(numbers)
print(list(rev))            # [9, 8, 7, 6, 5, 4, 3, 2, 1]

'''
Ten en cuenta que la lista 'numbers' permanece sin cambios con esta operación, y se mantiene en el mismo orden en que 
estaba originalmente. 
Para invertir la lista en su lugar, también puedes usar el método reverse. 
También puedes invertir una lista (obteniendo una copia, la lista original no se ve afectada) utilizando la sintaxis 
de slicing, estableciendo el tercer argumento (el paso) como -1.
'''
print(numbers[::-1])        # [9, 8, 7, 6, 5, 4, 3, 2, 1]
