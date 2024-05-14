'''
Numbers have four types in Python. Int, ﬂoat, complex, and long.
Numero tienen 4 tipos en Python: Int, float, complex y long(long ya no en python3)
'''

def function_numbers_data_type():
    int_num = 10            # int value
    print(type(int_num))
    float_num = 10.2        # float value
    print(type(float_num))
    complex_num = 3.14j     # complex value
    print(type(complex_num))
    #long_num = 1234567L     # long value , en Python 3 ya no existe Long
    #print(type(long_num))

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_numbers_data_type()