'''
Los programas de Python pueden leer de pipelines Unix. Aquí hay un ejemplo simple de cómo leer desde stdin:
'''

import sys
for linea in sys.stdin:
    print(linea)

''' Ten en cuenta que sys.stdin es un flujo. Esto significa que el bucle for solo terminará cuando el flujo haya 
finalizado.
Ahora puedes redirigir la salida de otro programa hacia tu programa de Python de la siguiente manera:

$ cat myfile | python myprogram.py

En este ejemplo, cat myfile puede ser cualquier comando Unix que produzca una salida en stdout.

Como alternativa, el módulo fileinput puede ser útil


import fileinput
for line in fileinput.input():
    process(line)
    
'''