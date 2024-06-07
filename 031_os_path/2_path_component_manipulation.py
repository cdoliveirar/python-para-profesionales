'''
Manipulación de Componentes de Ruta
'''

'''Para separar un componente de la ruta'''
import os

p = os.path.join(os.getcwd(), 'foo.txt')
print(p)
#'/Users/csaftoiu/tmp/foo.txt'
print(os.path.dirname(p))
# '/Users/csaftoiu/tmp'
print(os.path.basename(p))
# 'foo.txt'
print(os.path.split(os.getcwd()))
# ('/Users/csaftoiu/tmp', 'foo.txt')
print(os.path.splitext(os.path.basename(p)))
# ('foo', '.txt')

