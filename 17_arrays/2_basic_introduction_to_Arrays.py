'''
Un array es una estructura de datos que almacena valores del mismo tipo de dato. En Python, esta es la principal
diferencia entre arrays y listas. Mientras que las listas en Python pueden contener valores correspondientes a
diferentes tipos de datos, los arrays en Python solo pueden contener valores correspondientes al mismo tipo de dato.

En este tutorial, entenderemos los arrays en Python con los ejemplos.
Si eres nuevo en Python, comienza con el artículo de Introducción a Python.

Para usar arrays en el lenguaje Python, necesitas importar el módulo de array estándar. Esto se debe a que el array no
es un tipo de dato fundamental como las cadenas, los enteros, etc. Así es como puedes importar el módulo de array en
Python:

from array import *

Una vez que hayas importado el módulo de array, puedes declarar un array. Así es como lo haces:

arrayIdentifierName = array(typecode, [Initializers])

En la declaración anterior, "arrayIdentifierName" es el nombre del array, "typecode" le indica a Python el tipo de array
y "Initializers" son los valores con los que se inicializa el array.

Los "typecodes" son los códigos que se utilizan para definir el tipo de valores del array o el tipo de array. La tabla
en la sección de parámetros muestra los valores posibles que puedes usar al declarar un array y su tipo.

Aquí tienes un ejemplo del mundo real de declaración de un array en Python:

my_array = array('i',[1,2,3,4])

En el ejemplo anterior, el typecode utilizado es 'i'. Este typecode representa un entero firmado cuyo tamaño es de
2 bytes. Aquí tienes un ejemplo simple de un array que contiene 5 enteros:
'''

from array import *
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)

