'''
if condition:
    body
else:
    body

La declaración else ejecutará su cuerpo solo si todas las declaraciones condicionales anteriores se evalúan como False.
'''

if True:
    print("It is true!")                # Output: It is true!
else:
    print("This won't get printed..")


if False:
    print("This won't get printed..")
else:
    print("It is false!")               # Output: It is false!


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


