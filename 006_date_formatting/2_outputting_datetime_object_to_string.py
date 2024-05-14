'''
Uses C standard format codes.
usando en muchas aplicaciones
'''

def function_outputting_datetime_object_to_string():
    from datetime import datetime
    datetime_for_string = datetime(2016, 10, 1, 0, 0)
    datetime_string_format = '%b %d %Y, %H:%M:%S'
    datetime.strftime(datetime_for_string, datetime_string_format)
    strin_type = datetime.strftime(datetime_for_string, datetime_string_format)   #    Oct 01 2016, 00:00:00
    print(strin_type)
    print(type(strin_type))


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_outputting_datetime_object_to_string()