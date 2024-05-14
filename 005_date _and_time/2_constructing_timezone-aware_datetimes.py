'''
Por defecto, todos los objetos de fecha y hora son ingenuos. Para que tengan en cuenta la zona horaria,
debe adjuntar un objeto tzinfo, que proporciona la compensación UTC y la abreviatura de la zona horaria
en función de la fecha y la hora.
'''


def function_constructing_string_timezone():
    # Fixed Oﬀset Time Zones
    '''
    Para zonas horarias que tienen un desplazamiento fijo de UTC, en Python 3.2+, el módulo datetime proporciona
    la clase de zona horaria, una implementación concreta de tzinfo, que toma un timedelta y un parámetro
    de nombre (opcional):
    '''

    from datetime import datetime, timedelta, timezone
    JST = timezone(timedelta(hours=+9))
    print("JST: %s" % JST)

    dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
    print("Objeto dt %s" % dt)
    print(dt.tzname())          # UTC+09:00

    from dateutil import tz
    JST = tz.tzoffset('JST', 9 * 3600)  # 3600 seconds per hour
    print("JST 2: %s" % JST)
    dt = datetime(2015, 1, 1, 12, 0, tzinfo=JST)
    print(dt)
    print(dt.tzname)

    # Zonas con horario de verano

    local = tz.gettz()  # Local time
    PT = tz.gettz('US/Pacific')  # Pacific time
    dt_l = datetime(2015, 1, 1, 12, tzinfo=local)  # I am in EST
    dt_pst = datetime(2015, 1, 1, 12, tzinfo=PT)
    dt_pdt = datetime(2015, 7, 1, 12, tzinfo=PT)  # DST is handled automatically
    print(dt_l)
    print(dt_pst)
    print(dt_pdt)




# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_constructing_string_timezone()