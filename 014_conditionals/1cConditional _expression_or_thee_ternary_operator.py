'''
El operador ternario se utiliza para expresiones condicionales en línea. Se usa mejor en operaciones
simples y concisas que sean fáciles de leer.

- El orden de los argumentos es diferente al de muchos otros lenguajes (como C, Ruby, Java, etc.), lo que puede llevar
a errores cuando personas no familiarizadas con el "comportamiento sorprendente" de Python lo utilizan
(pueden invertir el orden).

Algunos lo encuentran "incómodo", ya que va en contra del flujo normal de pensamiento (pensar primero en la
condición y luego en los efectos).
'''

n = 5
print("Greater than 2" if n > 2 else "Smaller than or equal to 2")      # Out: 'Greater than 2'


'''
El resultado de esta expresión será tal como se lee en inglés: si la expresión condicional es Verdadera, entonces 
se evaluará como la expresión del lado izquierdo; de lo contrario, como la del lado derecho.

Las operaciones ternarias también pueden estar anidadas, como aquí
'''
n = 5
print("Hello" if n > 10 else "Goodbye" if n > 5 else "Good day")



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


