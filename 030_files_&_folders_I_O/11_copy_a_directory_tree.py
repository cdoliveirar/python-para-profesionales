'''
Copiar un árbol de directorios
'''

import shutil
source='//192.168.1.2/Daily Reports'
destination='D:\\Reports\\Today'
shutil.copytree(source, destination)


''' El directorio de destino no debe existir ya'''