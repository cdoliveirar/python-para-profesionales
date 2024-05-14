'''
Un bucle while hará que las declaraciones del bucle se ejecuten hasta que la condición del bucle sea falsa.
El siguiente código ejecutará las declaraciones del bucle un total de 4 veces
'''

i = 0
while i < 4:
    #loop statements
    print(i)
    i = i + 1

'''
Aunque el bucle anterior puede traducirse fácilmente en un bucle for más elegante, los bucles while son útiles para 
verificar si alguna condición se ha cumplido. El siguiente bucle seguirá ejecutándose hasta que myObject esté listo

myObject = anObject()
while myObject.isNotReady():
    myObject.tryToGetReady()
    
Los bucles while también pueden ejecutarse sin una condición utilizando números (complejos o reales) o True    
    
    
'''
import cmath
complex_num = cmath.sqrt(-1)
while complex_num:              # You can also replace complex_num with any number, True or a value of any type
    print(complex_num)          # Prints 1j forever


# Si la condición es siempre verdadera, el bucle while se ejecutará para siempre (bucle infinito) si no se termina
# con una instrucción break, return o una excepción.

while True:
    print("Infinite loop")

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



