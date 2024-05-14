'''
A menudo querrás asignar algo a un objeto si es None, lo que indica que no ha sido asignado. Utilizaremos
un objeto llamado aDate. La manera más simple de hacer esto es utilizando la prueba is None.
'''
import datetime

aDate = None

if aDate is None:           #   (Nota que es más "Pythonic" decir is None en lugar de == None.)
    aDate=datetime.date.today()
    print("La fecha")

'''
Pero esto se puede optimizar ligeramente aprovechando la noción de que not None se evaluará como True 
en una expresión booleana. El siguiente código es equivalente:
'''
aDate2 = None

if not aDate2:
    aDate2 = datetime.date.today()
    print("La fecha2")

# Pero hay una manera mas pytonica, el siguiente codifo es tambien equivalente !!!!!!!!!
aDate = aDate or datetime.date.today()
print(aDate)

'''
Esto realiza una evaluación de cortocircuito. Si aDate está inicializado y no es None, entonces se asigna a sí 
mismo sin ningún efecto neto. Si es None, entonces se asigna datetime.date.today() a aDate.
'''



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")


