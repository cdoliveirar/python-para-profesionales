'''
Copiando el contenido de un archivo a un diferente archivo
'''

with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
        out_file.write(line)

# usando el modulo shutil
import shutil
shutil.copyfile(src, dst)

