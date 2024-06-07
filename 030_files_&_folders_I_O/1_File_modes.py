'''
Parameter                                           Details
ﬁlename:    La ruta de tu archivo o, si el archivo está en el directorio de trabajo, el nombre de archivo de tu archivo
access_mode: Un valor de cadena que determina cómo se abre el archivo
buﬀering:   Un valor entero usado para el almacenamiento temporal de líneas, opcional. (buﬀering)
'''

'''Cuando se trata de almacenar, leer o comunicar datos, trabajar con los archivos de un sistema operativo es tanto 
necesario como fácil con Python. A diferencia de otros lenguajes donde la entrada y salida de archivos requiere 
la lectura y escritura de objetos complejos, Python simplifica el proceso solo necesitando comandos para abrir, 
leer/escribir y cerrar el archivo. Te explico cómo Python puede interactuar con archivos en el sistema operativo.'''

''' Hay diferentes modos con los que puedes abrir un archivo, especificados por el parámetro de modo. Estos incluyen'''

'''
'r' - modo de lectura. Es el modo predeterminado. Solo te permite leer el archivo, no modificarlo. Cuando se usa este 
    modo, el archivo debe existir.

'w' - modo de escritura. Creará un nuevo archivo si no existe, de lo contrario, borrará el archivo y te permitirá 
    escribir en él.

'a' - modo de añadir. Escribirá datos al final del archivo. No borra el archivo y el archivo debe existir para este 
    modo.

'rb' - modo de lectura en binario. Es similar a 'r' excepto que la lectura se fuerza en modo binario. Esta también es 
    una elección predeterminada.

'r+' - modo de lectura más modo de escritura al mismo tiempo. Esto te permite leer y escribir en archivos al mismo 
    tiempo sin tener que usar 'r' y 'w'.

'rb+' - modo de lectura y escritura en binario. Igual que 'r+' excepto que los datos están en binario.

'wb' - modo de escritura en binario. Igual que 'w' excepto que los datos están en binario.

'w+' - modo de escritura y lectura. Exactamente lo mismo que 'r+' pero si el archivo no existe, se crea uno nuevo. 
    De lo contrario, el archivo se sobrescribe.

'wb+' - modo de escritura y lectura en binario. Igual que 'w+' pero los datos están en binario.

'ab' - modo de añadir en binario. Similar a 'a' excepto que los datos están en binario.

'a+' - modo de añadir y leer. Similar a 'w+' ya que creará un nuevo archivo si el archivo no existe. De lo contrario, 
    el puntero del archivo está al final del archivo si existe.

'ab+' - modo de añadir y leer en binario. Igual que 'a+' excepto que los datos están en binario.

with open(filename, 'r') as f:
    f.read()
with open(filename, 'w') as f:
    f.write(filedata)
with open(filename, 'a') as f:
    f.write('\\n' + newdata)

                    r       r+      w       w+      a       a+
Read                ✔       ✔       ✘       ✔       ✘       ✔
Write               ✘       ✔       ✔       ✔       ✔       ✔
Creates ﬁle         ✘       ✘       ✔       ✔       ✔       ✔
Erases ﬁle          ✘       ✘       ✔       ✔       ✘       ✘    
Initial position    Start   Start   Start   Start   End     End
'''

'''
Python 3 añadió un nuevo modo para la creación exclusiva, de manera que accidentalmente no trunques o sobreescribas 
un archivo existente.

'x' - abrir para creación exclusiva, generará FileExistsError si el archivo ya existe.
'xb' - abrir para creación exclusiva en modo de escritura en binario. Igual que 'x' excepto que los datos están en 
binario.
'x+' - modo de lectura y escritura. Similar a 'w+' ya que creará un nuevo archivo si el archivo no existe. De lo 
contrario, generará FileExistsError.
'xb+' - modo de escritura y lectura. Exactamente igual que 'x+' pero los datos están en binario.

                    x       x+
Read                ✘       ✔            
Write               ✔       ✔
Creates ﬁle         ✔       ✔
Erases ﬁle          ✘       ✘      
Initial position    Start   Start    

Permite escribir el código de apertura de archivos de una manera más pitónica:
'''

try:
    with open("fname", "r") as fout:
        '''Trabajar con tu fichero abierto'''
except FileExistsError:
        '''Tu manejo de erroo va aqui'''
