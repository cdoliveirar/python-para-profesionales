def function_creating_a_module():
    pass
    # Functions in a module can be used by importing the module.

    # Para los módulos que haya creado, deberán estar en el mismo directorio que el archivo que los está importando.
    # en. (Sin embargo, también puede colocarlos en el directorio lib de Python con los módulos preincluidos, pero debería ser
    # evitarse si es posible.)

    import hello
    hello.say_hello()

    # Modules can be imported by other modules.
    # Speciﬁc functions of a module can be imported.
    from hello import say_hello
    say_hello()

    # modulo pueden tener alias
    import hello as he
    he.say_hello()



if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_creating_a_module()

    # Un módulo puede ser un script ejecutable independiente.
    from hello import say_hello
    say_hello()
