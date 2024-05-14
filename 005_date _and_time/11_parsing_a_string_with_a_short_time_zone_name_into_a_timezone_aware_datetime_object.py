'''
Using the dateutil library as in the previous example on parsing timezone-aware timestamps, it is also possible to
parse timestamps with a speciﬁed "short" time zone name.

Para fechas formateadas con abreviaturas o nombres cortos de zona horaria, que generalmente son ambiguos
(por ejemplo, CST, que podría ser la hora estándar central, la hora estándar de China, la hora estándar de Cuba,
etc. (puede encontrar más información aquí) o no necesariamente disponible en una base de datos estándar,
es necesario especificar una asignación entre la abreviatura de la zona horaria y objeto tzinfo.
'''


def function_arsing_a_string_with_a_short_time_zone():
    from dateutil import tz
    from dateutil.parser import parse

    ET = tz.gettz('US/Eastern')
    CT = tz.gettz('US/Central')
    MT = tz.gettz('US/Mountain')
    PT = tz.gettz('US/Pacific')

    us_tzinfos = {  'CST': CT, 'CDT': CT,
                    'EST': ET, 'EDT': ET,
                    'MST': MT, 'MDT': MT,
                    'PST': PT, 'PDT': PT
                 }


    dt_est = parse('2014-01-02 04:00:00 EST', tzinfos=us_tzinfos)
    dt_pst = parse('2016-03-11 16:00:00 PST', tzinfos=us_tzinfos)

    print(dt_est)
    print(dt_pst)

    # Vale la pena señalar que si utiliza una zona horaria de pytz con este método, no se localizará correctamente:
    import pytz
    EST = pytz.timezone('America/New_York')
    dt = parse('2014-02-03 09:17:00 EST', tzinfos={'EST': EST})

    # This simply attaches the pytz time zone to the datetime:
    dt.tzinfo  # Will be in Local Mean Time!
    # <DstTzInfo 'America/New_York' LMT-1 day, 19:04:00 STD>

    # If using this method, you should probably re- localize the naive portion of the datetime after parsing:
    dt_fixed = dt.tzinfo.localize(dt.replace(tzinfo=None))
    dt_fixed.tzinfo  # Now it's EST.
    # <DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_arsing_a_string_with_a_short_time_zone()