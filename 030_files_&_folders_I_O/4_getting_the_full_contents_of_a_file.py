'''
Obteniendo el contenido completo de un archivo
'''

''' El método preferido para la entrada/salida de archivos es usar la palabra clave "with". Esto asegurará que el 
manejador del archivo se cierre una vez que la lectura o escritura haya sido completada'''

with open('myfile.txt') as in_file:
    content = in_file.read()
print(content)

''' o, para manejar el cierre del archivo manualmente, puedes prescindir de "with" y simplemente llamar a "close" 
tú mismo:'''

in_file = open('myfile.txt', 'r')
content = in_file.read()
print(content)
in_file.close()

''' Ten en cuenta que sin usar una declaración "with", podrías mantener el archivo abierto accidentalmente en caso de 
que surja una excepción inesperada así:'''

in_file = open('myfile.txt', 'r')
raise Exception("oops")
in_file.close() # este codigo nunca será llamado.

''' una solucion seria poner todo este codigo dentro de un try/catch'''
in_file = open('myfile.txt', 'r')
try:
    raise Exception("oops")
finally:
    in_file.close()

