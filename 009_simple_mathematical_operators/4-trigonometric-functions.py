import math
'''

'''

def trigonometric_functions():
    a, b = 1, 2

    print(math.sin(a))  # Retorna el seno de a en radianes

    print(math.cosh(b)) # Devuelve el coseno hiperbólico inverso de 'b' en radianes

    print(math.atan(math.pi))   # Devuelve la tangente inversa de 'pi' en radianes

    print(math.hypot(a, b))     # Devuelve la norma euclidiana, igual que math.sqrt(aa + bb)


    # Para convertir de radianes a grados y de grados a radianes, respectivamente, se utilizan las funciones
    # math.degrees y math.radians
    print(math.degrees(a))      # 57.29577951308232

    print(math.radians(57.29577951308232))  # 1.0
    








if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    trigonometric_functions()