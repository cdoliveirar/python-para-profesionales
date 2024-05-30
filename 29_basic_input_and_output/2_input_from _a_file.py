'''
La entrada también se puede leer desde archivos. Los archivos se pueden abrir utilizando la función incorporada open.
Usar la sintaxis with <comando> as <nombre> (llamada 'Administrador de Contexto') hace que usar open y obtener un
manejador para el archivo sea muy fácil:
'''

#with open('somefile.txt', 'r') as fileobj:
    # escribe el código aquí usando fileobj


''' Esto asegura que cuando la ejecución del código salga del bloque, el archivo se cerrará automáticamente.

Los archivos se pueden abrir en diferentes modos. En el ejemplo anterior, el archivo se abre solo para lectura. 
Para abrir un archivo existente solo para lectura, usa r. Si quieres leer ese archivo como bytes, usa rb. Para agregar 
datos a un archivo existente, usa a. Usa w para crear un archivo o sobrescribir cualquier archivo existente con el 
mismo nombre. Puedes usar r+ para abrir un archivo tanto para lectura como para escritura. 

El primer argumento de open() es el nombre del archivo, el segundo es el modo. Si el modo se deja en blanco, el valor 
predeterminado será r.
'''

# Vamos a crear un archivo ejemplo:
with open('shoppinglist.txt', 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')

with open('shoppinglist.txt', 'r') as fileobj:
    # Este método crea una lista donde cada línea del archivo es un elemento de la lista.
    lines = fileobj.readlines()

print(lines)        # ['tomato\n', 'pasta\n', 'garlic']

with open('shoppinglist.txt', 'r') as fileobj:
    # Aquí leemos todo el contenido en una sola cadena
    content = fileobj.read()
    # obteniendo una lista de líneas, igual que en el ejemplo anterior
    lines = content.split('\n')     # usa para dividir una cadena en una lista de subcadenas basándose en un delimitador

print(type(content))    # <class 'str'>
print(type(lines))      # <class 'list'>
print(lines)


''' Si el tamaño del archivo es pequeño, es seguro leer todo el contenido del archivo en la memoria. Si el archivo es 
muy grande, a menudo es mejor leer línea por línea o por fragmentos, y procesar la entrada en el mismo bucle. 
Para hacer eso'''

with open('shoppinglist.txt', 'r') as fileobj:
    # this method reads line by line:
    lines = []
    for line in fileobj:
        lines.append(line.strip()) # eliminar los caracteres en blanco (espacios, tabulaciones, nuevas líneas) del
                                   # principio y del final de una cadena
print(lines)        # ['tomato', 'pasta', 'garlic']

'''  Al leer archivos, ten en cuenta los caracteres de salto de línea específicos del sistema operativo. Aunque for 
line in fileobj los elimina automáticamente, siempre es seguro llamar a strip() en las líneas leídas, como se muestra 
arriba.

Los archivos abiertos (fileobj en los ejemplos anteriores) siempre apuntan a una ubicación específica en el archivo. 
Cuando se abren por primera vez, el manejador de archivos apunta al principio del archivo, que es la posición 0. 
El manejador de archivos puede mostrar su posición actual con tell '''

fileobj = open('shoppinglist.txt', 'r')
pos = fileobj.tell()
print('We are at %u.' % pos) # We are at 0.

''' Al leer todo el contenido, la posición del manejador de archivos estará al final del archivo.'''
content = fileobj.read()
end = fileobj.tell()
print('This file was %u characters long.' % end)  # This file was 19 characters long.
fileobj.close()


''' La posición del manejador de archivos se puede establecer en lo que sea necesario:'''
fileobj = open('shoppinglist.txt', 'r')
fileobj.seek(7)
pos = fileobj.tell()
print('We are at character #%u.' % pos) # We are at character #7.

''' También puedes leer cualquier longitud del contenido del archivo durante una llamada dada. Para hacer esto, pasa 
un argumento a read().

Cuando read() se llama sin argumento, leerá hasta el final del archivo. Si pasas un argumento, leerá ese número de 
bytes o caracteres, dependiendo del modo (rb y r, respectivamente).'''

# lee los próximos 4 caracteres
# comenzando en la posición actual
next4 = fileobj.read(4)
# ¿qué obtuvimos?
print(next4)        # past
# ¿dónde estamos ahora?
pos = fileobj.tell()
print('Estamos en %u.' % pos) # Estamos en 11, ya que estábamos en 7, y leímos 4 caracteres.
fileobj.close()


''' Para demostrar la diferencia entre caracteres y bytes:'''
with open('shoppinglist.txt', 'r') as fileobj:
    print(type(fileobj.read()))             # <class 'str'>
with open('shoppinglist.txt', 'rb') as fileobj:
    print(type(fileobj.read()))             # <class 'bytes'>