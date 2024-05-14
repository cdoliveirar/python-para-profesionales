'''
Uses C standard format codes.
'''

def function_parsing_string_to_datetime_object():
    from datetime import datetime
    datetime_string = 'Oct 1 2016, 00:00:00'
    datetime_string_format = '%b %d %Y, %H:%M:%S'
    datetime.strptime(datetime_string, datetime_string_format)
    date_time_object = datetime.strptime(datetime_string, datetime_string_format)  # 2016-10-01 00:00:00
    print(date_time_object)
    print(type(date_time_object))

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_parsing_string_to_datetime_object()