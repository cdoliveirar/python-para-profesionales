'''
Imprimiendo una cadena sin un salto de línea al final
'''

''' La función print tiene un parámetro opcional llamado end que es lo que imprime al final de la cadena dada. 
Por defecto, es un carácter de salto de línea, por lo que es equivalente a esto'''

print("Hello, ", end="\n")
print("World!")
# Hello,
# World!

''' Por defecto, end está configurado en "\n", que representa un salto de línea. Por lo tanto, cada vez que se imprime 
algo con print, se agrega automáticamente un salto de línea al final.'''

print("Hello, ", end="")
print("World!")
# Hello, World!

print("Hello, ", end="<br>")
print("World!")
# Hello, <br>World!

print("Hello, ", end="BREAK")
print("World!")
# Hello, BREAKWorld!

import sys
sys.stdout.write("Hello, ")
sys.stdout.write("World!")

# Hello, World!