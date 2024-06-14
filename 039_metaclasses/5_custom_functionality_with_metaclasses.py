'''
Funcionalidad personalizada con metaclases
'''

''' La funcionalidad en las metaclases puede modificarse de modo que cada vez que se construya una clase, se imprima 
una cadena en la salida estándar o se lance una excepción. Esta metaclase imprimirá el nombre de la clase que se está 
construyendo.'''

class MetaclaseVerbosa(type):
    def __new__(cls, nombre_clase, padres_clase, dict_clase):
        print("Creando clase ", nombre_clase)
        nueva_clase = super().__new__(cls, nombre_clase, padres_clase, dict_clase)
        return nueva_clase

''' Puedes usar la metaclase de la siguiente manera:'''

class Spam(metaclass=MetaclaseVerbosa):
    def eggs(self):
        print("[inserte cadena de ejemplo aquí]")

s = Spam()
s.eggs()

# Creando clase  Spam
# [inserte cadena de ejemplo aquí]