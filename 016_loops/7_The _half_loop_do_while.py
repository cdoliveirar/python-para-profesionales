'''
A diferencia de otros lenguajes, Python no tiene una construcción do-until o do-while (esto permitiría que el código
se ejecutara una vez antes de que se probara la condición). Sin embargo, puedes combinar un while True con un break
para lograr el mismo propósito
'''

a = 10
while True:
    a = a-1
    print(a)
    if a < 7:
        break
print('Done.')


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")



