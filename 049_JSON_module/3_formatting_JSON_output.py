'''
Formateando la salida JSON
'''

import json
''' Supongamos que tenemos los siguientes datos'''

data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}

''' Simplemente volcar esto como JSON no hace nada especial aquí'''

print(json.dumps(data))     # Devuelve la representación JSON como una cadena en lugar de escribirla en un archivo
# {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}

''' * Ajustar la indentación para obtener una salida más bonita'''

''' Si queremos una impresión bonita, podemos establecer un tamaño de sangría'''
print(json.dumps(data, indent=2))
# {
#   "cats": [
#     {
#       "name": "Tubbs",
#       "color": "white"
#     },
#     {
#       "name": "Pepper",
#       "color": "black"
#     }
#   ]
# }

''' * Ordenar las claves alfabéticamente para obtener un resultado consistente'''

''' Por defecto, el orden de las claves en la salida no está definido. Podemos ordenarlas alfabéticamente para 
asegurarnos de obtener siempre la misma salida'''

print(json.dumps(data, sort_keys=True))
# {"cats": [{"color": "white", "name": "Tubbs"}, {"color": "black", "name": "Pepper"}]}


''' * Eliminar los espacios en blanco para obtener una salida compacta.

Es posible que deseemos eliminar los espacios innecesarios, lo cual se logra configurando cadenas separadoras 
diferentes a las predeterminadas ', ' y ': '.'''

print(json.dumps(data, separators=(',', ':')))
# {"cats":[{"name":"Tubbs","color":"white"},{"name":"Pepper","color":"black"}]}
