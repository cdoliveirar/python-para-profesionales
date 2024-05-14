'''
Este comportamiento se puede extender. Aquí hay un arreglo tridimensional
'''

lst  = [[[111,112,113],[121,122,123],[131,132,133]],[[211,212,213],[221,222,223],[231,232,233]],[[311,312, 313],[321,322,323],[331,332,333]]]

'''
Como probablemente sea obvio, esto se vuelve un poco difícil de leer. Usa barras invertidas para dividir las 
diferentes dimensiones.
'''

myarray  = [[[111,112,113],[121,122,123],[131,132,133]],\
        [[211,212,213],[221,222,223],[231,232,233]],\
        [[311,312,313],[321,322,323],[331,332,333]]]

'''
Al anidar las listas de esta manera, puedes extenderlas a dimensiones arbitrariamente altas. El acceso es similar a 
los arreglos 2D:
'''

print(myarray)
print(" ")
print(myarray[1])
print(" ")
print(myarray[2][1])
print(" ")
print(myarray[1][0][2])

'''
Y la edición también es similar.

myarray[1]=new_n-1_d_list
myarray[2][1]=new_n-2_d_list
myarray[1][0][2]=new_n-3_d_list

'''