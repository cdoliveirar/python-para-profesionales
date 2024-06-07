'''
Leer un archivo linea por linea
'''

''' La manera más simple de iterar sobre un archivo línea por línea '''
with open('myfile.txt', 'r') as fp:
    for line in fp:
        print(line)

'''readline() permite un control más granular sobre la iteración línea por línea. El ejemplo a continuación es 
equivalente al anterior. '''

with open('myfile.txt', 'r') as fp:
    while True:
        cur_line = fp.readline()
# If the result is an empty string
        if cur_line == '':
# We have reached the end of the file
            break
        print(cur_line)


''' Usar el iterador for loop y readline() juntos se considera una mala práctica. Más comúnmente, se utiliza el método 
readlines() para almacenar una colección iterable de las líneas del archivo'''

with open("myfile.txt", "r") as fp:
    lines = fp.readlines()
    print(lines)
for i in range(len(lines)):
    print("Line " + str(i) + ": " + lines[i])

