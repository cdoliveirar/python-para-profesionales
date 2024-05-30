'''
Las tuplas son comparables e igualables elemento por elemento."

'''

hash( (1, 2) )                  # ok
hash( ([], {"hello"}))          # TypeError: unhashable type: 'list'

''' Para que un objeto sea "hashable" en Python, debe ser inmutable y debe implementar los métodos __hash__ y __eq__. 
Los objetos mutables como listas y conjuntos no son hashables porque sus contenidos pueden cambiar, lo que afectaría 
su hash y causaría inconsistencias en estructuras de datos como conjuntos (set) o diccionarios (dict) que dependen 
de hashes.'''

{ (1, 2) }  # Este código es válido y no generará un error porque las tuplas son inmutables y, por lo tanto, hashables.