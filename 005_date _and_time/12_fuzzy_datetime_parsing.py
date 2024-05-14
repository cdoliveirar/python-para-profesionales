'''
It is possible to extract a date out of a text using the dateutil parser in a "fuzzy" mode, where components of
the string not recognized as being part of a date are ignored.
'''


def function_fuzzy_datetime_parsing():
    from dateutil.parser import parse
    dt = parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True)
    print(dt)       # 2047-01-01 08:21:00

    # dt is now a datetime object and you would see datetime.datetime(2047, 1, 1, 8, 21) printed.
    

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_fuzzy_datetime_parsing()