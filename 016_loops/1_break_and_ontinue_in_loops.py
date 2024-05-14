'''
Sentencia break:
Cuando una sentencia break se ejecuta dentro de un bucle, el flujo de control "rompe" el bucle inmediatamente.
'''

i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

'''
La condición del bucle no se evaluará después de que se ejecute la sentencia break. Ten en cuenta que las 
sentencias break solo están permitidas dentro de bucles, sintácticamente. Una sentencia break dentro de una 
función no puede utilizarse para terminar bucles que hayan llamado a esa función.

Ejecutar lo siguiente imprime cada dígito hasta el número 4, momento en el que se encuentra la sentencia break y el bucle se detiene.

0
1
2
3
4
Breaking from loop
'''

# Las sentencias break también pueden ser utilizadas dentro de bucles for, la otra estructura de bucle proporcionada
# por Python.
for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break

# Si un bucle tiene una cláusula else, esta no se ejecuta cuando el bucle se termina mediante una sentencia break.

'''
sentencia continue:

Una sentencia continue saltará a la próxima iteración del bucle, evitando el resto del bloque actual pero continuando 
con el bucle. Al igual que con break, continue solo puede aparecer dentro de bucles.
'''
print("sentencia continue:")

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)

'''
Ten en cuenta que 2 y 4 no se imprimen, esto se debe a que continue pasa a la siguiente iteración en lugar 
de continuar con print(i) cuando i == 2 o i == 4.
'''

# Bucles anidados (Nested Loops)
print("Bucles anidados")
'''
break y continue solo operan en un solo nivel de bucle. El siguiente ejemplo solo romperá el bucle interno for, 
no el bucle externo while.
'''
'''while True:
    for i in range(1,5):
        print(i)
        if i == 2:
            break           # ¡Solo romperá el bucle interno!
'''
'''
Python no tiene la capacidad de salir de múltiples niveles de bucles a la vez; si se desea este comportamiento, 
refactorizar uno o más bucles en una función y reemplazar break con return puede ser la solución.
'''


# Utiliza return dentro de una función como si fuera un break.
# La declaración return sale de una función sin ejecutar el código que viene después de ella.
print("uso de return")
'''
Si tienes un bucle dentro de una función, utilizar return desde dentro de ese bucle es equivalente a tener un break, 
ya que el resto del código del bucle no se ejecuta (ten en cuenta que tampoco se ejecuta ningún código después 
del bucle).
'''
def break_loop():
    for i in range(1, 5):
        print(i)
        if (i == 2):
            return(i)
        print(i)
    return(5)

# Si tienes bucles anidados, la declaración return romperá todos los bucles.
def break_all():
    for j in range(1, 5):
        print(j)
        for i in range(1,4):
            print(i)
            if i*j == 6:
                return(i)
        print(i*j)

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    break_loop()
    break_all()



