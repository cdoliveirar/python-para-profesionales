'''
En Python puedes definir una serie de condicionales usando 'if' para el primero, 'elif' para los siguientes,
hasta llegar al final (opcional) 'else' para cualquier cosa que no sea capturada por las otras condiciones.
'''

number = 5
if number > 2:
    print("Number is bigger than 2.")
elif number < 2:        # Optional clause (Puedes tener múltiples 'elif')
    print("Number is smaller than 2.")
else:                   # Optional clause (Solo puedes tener un 'else')
    print("Number is 2.")

# Usar "else if" en lugar de "elif" provocará un error de sintaxis y no está permitido.

if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


