'''
El diccionario consta de pares clave-valor. Está encerrado entre llaves {} y se pueden asignar y acceder a los valores.
usando corchetes [].
'''


def function_dictionary_data_type():
    dic = {'name': 'red', 'age': 10}
    print(dic)                  # will output all the key-value pairs. {'name':'red','age':10}
    print(dic['name'])          # will output only value with 'name' key. 'red'
    print(dic.values())         # will output list of values in dic. ['red',10]
    print(dic.keys())           # will output list of keys. ['name','age']


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_dictionary_data_type()