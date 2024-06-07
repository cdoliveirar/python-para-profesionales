'''
Escribiendo a un archivo
'''

with open('myfile2.txt', 'w') as f:
    f.write("Line 1")
    f.write("Line 2")
    f.write("Line 3")
    f.write("Line 4")


''' Si abres el fichero veras el contenido de esta forma:

Line 1Line 2Line 3Line 4
'''

''' Python automaticamente no agrega saltos de linea, necesitas hacerlo manuelmente'''

with open('myfile2.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4\n")

'''No uses os.linesep como un terminador de línea al escribir archivos abiertos en modo texto (el modo predeterminado);
usa \n en su lugar.
Si deseas especificar una codificación, simplemente añade el parámetro encoding a la función open
'''

with open('my_file.txt', 'w', encoding='utf-8') as f:
    f.write('utf-8 text')

''' También es posible usar la instrucción print para escribir en un archivo. La mecánica es diferente en Python 2 en 
comparación con Python 3, pero el concepto es el mismo: puedes tomar la salida que se hubiera mostrado en la pantalla y 
enviarla a un archivo en su lugar'''

with open('fred.txt', 'w') as outfile:
    s = "I'm Not Dead Yet!"
    print(s) # writes to stdout
    print(s, file = outfile) # writes to outfile
    myfile = None
    print(s, file = myfile) # writes to stdout, print(s, file=None) es equivalente a print(s)
    print(s, file = None) # writes to stdout,  print(s, file=None) es equivalente a print(s)

