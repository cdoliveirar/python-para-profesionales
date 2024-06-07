'''
Ruta absoluta desde una ruta relativa
'''

# Use os.path.abspath :
import os
print(os.getcwd())
# '/Users/csaftoiu/tmp'
print(os.path.abspath('foo'))
# '/Users/csaftoiu/tmp/foo'
print(os.path.abspath('../foo'))
# '/Users/csaftoiu/foo'
print(os.path.abspath('/foo'))

