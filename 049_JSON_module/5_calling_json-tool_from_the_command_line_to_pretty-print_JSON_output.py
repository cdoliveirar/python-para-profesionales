'''
Llamar a json.tool desde la línea de comandos para
imprimir en formato legible el output de JSON
'''

''' Dado un archivo JSON "foo.json" como
    {"foo": {"bar": {"baz": 1}}}
'''

''' 
podemos llamar al módulo directamente desde la línea de comandos (pasando el nombre del archivo como argumento) 
para imprimirlo en formato legible

$ python -m json.tool foo.json
'''

{
    "foo": {
        "bar": {
            "baz": 1
        }
    }
}




''' El módulo también tomará la entrada desde STDOUT, así que (en Bash) igualmente podríamos hacer'''

{
    "foo": {
        "bar": {
            "baz": 1
        }
    }
}


