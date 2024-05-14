'''
Los siguientes valores se consideran falsos, en el sentido de que se evalúan como False cuando se aplican a un
operador booleano.
'''

#   None
#  False
#  0 , or any numerical value equivalent to zero, for example 0L , 0.0 , 0j
#  Empty sequences: '', "", (), []
#  Empty mappings: {}
#  User-deﬁned types where the __bool__ or __len__ methods return 0 or False


#   All other values in Python evaluate to True .

'''
Nota: Un error común es simplemente verificar la falsedad de una operación que devuelve diferentes valores falsos 
donde la diferencia importa. Por ejemplo, usar if foo() en lugar de la forma más explícita if foo() is None
'''


if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


