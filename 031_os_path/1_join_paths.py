'''
Este módulo implementa algunas funciones útiles para los nombres de ruta. Los parámetros de ruta pueden pasarse como
cadenas de texto o bytes. Se recomienda que las aplicaciones representen los nombres de archivo como cadenas de
caracteres (Unicode).
'''

''' Para unir dos o más componentes de ruta, primero importa el módulo os de Python y luego utiliza lo siguiente:'''

import os
print(os.path.join('a', 'b', 'c'))      # a/b/c

''' La ventaja de usar os.path es que permite que el código siga siendo compatible en todos los sistemas operativos, 
ya que utiliza el separador apropiado para la plataforma en la que se está ejecutando.
Por ejemplo, el resultado de este comando en Windows será:

os.path.join('a', 'b', 'c')
'a\b\c'
'''

# Unix OS a/b/c

