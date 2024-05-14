'''
pass es una declaración nula que se utiliza cuando la sintaxis de Python requiere una declaración (como dentro del
cuerpo de un bucle for o while), pero no se requiere ni se desea ninguna acción por parte del programador.
Esto puede ser útil como marcador de posición para código que aún no se ha escrito
'''

for x in range(10):
    pass

'''
En este ejemplo, no sucederá nada. El bucle for se completará sin errores, pero no se ejecutarán comandos ni código. 
pass nos permite ejecutar nuestro código correctamente sin tener todas las instrucciones y acciones completamente 
implementadas. 
Del mismo modo, pass se puede utilizar en bucles while, así como en selecciones y definiciones de funciones, etc.

while x == y:
    pass
'''


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



