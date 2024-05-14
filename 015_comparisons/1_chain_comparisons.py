'''
Puedes comparar varios elementos con múltiples operadores de comparación utilizando la comparación encadenada
(chain comparison)
'''

#   x > y > z

#   esto es una forma abreviada de:

#   x > y and y > z
# Esto se evaluará como Verdadero solo si ambas comparaciones son Verdaderas.

# La forma general es:
# a OP b OP c OP d ...
# Where OP represents one of the multiple comparison operations you can use, and the letters represent arbitrary
# valid expressions.


'''
Ten en cuenta que 0 != 1 != 0 evalúa a True, incluso aunque 0 != 0 es False. A diferencia de la notación matemática 
común en la que x != y != z significa que x, y z tienen valores diferentes. Encadenar operaciones == tiene el 
significado natural en la mayoría de los casos, ya que la igualdad es generalmente transitiva. 
(si A == B y B == C, entonces A == C)"
'''
print(0 != 1 != 0) # True , incluso aunque 0 != 0 es False


#   Estilo
#   ------
'''
No hay un límite teórico en la cantidad de elementos y operaciones de comparación que puedes usar siempre y 
cuando tengas una sintaxis adecuada.
'''
print(1 > -1 < 2 > 0.5 < 100 != 24)
'''
Lo anterior devuelve True si cada comparación devuelve True. Sin embargo, usar encadenamientos complicados 
no es un buen estilo. Un encadenamiento bueno será "directional", no más complicado que eso.
'''
x= 2
y= -5
print(1 > x > -4 > y != 8)

# Efectos secundarios (Side eﬀects )
# ----------------------------------
'''
Tan pronto como una comparación devuelva False, la expresión se evalúa inmediatamente como False, 
omitiendo todas las comparaciones restantes.

Ten en cuenta que la expresión exp en a > exp > b se evaluará solo una vez, mientras que en el caso de

a > exp and exp > b

exp será calculada dos veces si a > exp es verdadero.
'''


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



