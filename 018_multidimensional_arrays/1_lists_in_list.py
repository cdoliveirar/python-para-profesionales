'''
Una buena manera de visualizar un arreglo 2D es como una lista de listas. Algo así:
'''
lst=[[1,2,3],[4,5,6],[7,8,9]]
'''
Aquí, la lista externa lst tiene tres elementos. Cada uno de esos elementos es otra lista: El primero es: [1,2,3],
el segundo es: [4,5,6] y el tercero es: [7,8,9]. Puedes acceder a estas listas de la misma manera que accederías a
cualquier otro elemento de una lista, así:
'''
print (lst[0])
#output: [1, 2, 3]
print (lst[1])
#output: [4, 5, 6]
print (lst[2])
#output: [7, 8, 9]

'''
puedes acceder a los diferentes elementos en cada una de esas listas de la misma manera:
'''
print (lst[0][0])
#output: 1
print (lst[0][1])
#output: 2

'''
Aquí, el primer número dentro de los corchetes [] significa obtener la lista en esa posición. En el ejemplo anterior, 
usamos el número 0 para obtener la lista en la posición 0, que es [1,2,3]. El segundo conjunto de corchetes [] 
significa obtener el elemento en esa posición de la lista interna. En este caso, usamos tanto 0 como 1; la posición 0 
en la lista que obtuvimos es el número 1 y en la posición 1 es 2.

También puedes set valores dentro de estas listas de la misma manera
'''
lst[0]=[10,11,12]
lst[1][2]=15
print(lst[0])
print(lst)

'''
Ahora la lista es [[10,11,12],[4,5,15],[7,8,9]]. En este ejemplo, cambiamos un solo elemento dentro de una de las 
listas internas. Primero ingresamos en la lista en la posición 1 y cambiamos el elemento dentro de ella en la 
posición 2, que era 6 y ahora es 15
'''


