'''
Elemento más pequeño en una colección

La propiedad más interesante de un heap es que su elemento más pequeño siempre es el primer elemento: heap[0].
'''
import heapq
numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]

heapq.heapify(numbers)
print(numbers)          # [2, 4, 10, 100, 8, 50, 32, 200, 150, 20]

#           2
#        /    \
#       4      8
#      / \    / \
#    100 10  50  32
#    / \  /
#  200 150 20
''' En un heap mínimo, cada nodo padre es menor o igual que sus nodos hijos.'''


heapq.heappop(numbers) # 2
print(numbers)           # [4, 8, 10, 100, 20, 50, 32, 200, 150]

#         4
#       /   \
#      10    8
#     / \   / \
#   100 20 50 32
#   / \
# 200 150