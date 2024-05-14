'''
La funciónes implementan operaciones similares al operador and y or:
'''


'''
Cuando usas "or", devolverá el primer valor en la expresión si es verdadero, de lo contrario,
devolverá ciegamente el segundo valor.
'''
def or_(a, b):
    if a:
        return a
    else:
        return b

'''
Para "and", devolverá su primer valor si es falso; de lo contrario, devolverá el último valor
'''
def and_(a, b):
    if not a:
        return a
    else:
        return b


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    print("   OR")
    orr = or_(False,True)
    print(orr)
    orr = or_(True, False)
    print(orr)
    orr = or_(False, False)
    print(orr)
    print("   AND")
    andd = and_(False, True)
    print(andd)
    andd = and_(True, False)
    print(andd)
    andd = and_(True, True)
    print(andd)
