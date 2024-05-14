'''
Python solo tiene soporte limitado para analizar marcas de tiempo ISO 8601. Para strptime necesitas saber exactamente qué
formato en el que se encuentra. Como complicación, la cadena de fecha y hora es una marca de tiempo ISO 8601, con espacio como
separador y fracción de 6 dígitos:
'''

import datetime

def function_parsing_arbitraryISO8601():
    a = str(datetime.datetime(2016, 7, 22, 9, 25, 59, 555555))
    print(a)
    a = str(datetime.datetime(2016, 7, 22, 9, 25, 59, 0))
    print(a)

    # There is a single-ﬁle library called iso8601 which properly parses ISO 8601 timestamps and only them.
    #import iso8601
    #iso8601.parse_date('2016-07-22 09:25:59')
    # datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)

    #iso8601.parse_date('2016-07-22 09:25:59+03:00')
    # datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<FixedOffset '+03:00' ...>)

    #iso8601.parse_date('2016-07-22 09:25:59Z')
    # datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)

    #iso8601.parse_date('2016-07-22T09:25:59.000111+03:00')
    # datetime.datetime(2016, 7, 22, 9, 25, 59, 111, tzinfo=<FixedOffset '+03:00' ...>)

    #iso8601.parse_date('2016-07-22T09:25:59', default_timezone=None)
    # datetime.datetime(2016, 7, 22, 9, 25, 59)

    #iso8601.parse_date('2016-07-22T09:25:59Z', default_timezone=None)
    # datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_parsing_arbitraryISO8601()