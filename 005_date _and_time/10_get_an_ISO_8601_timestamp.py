'''

'''



def function_10_get_an_ISO_8601_timestamp():
    # Without timezone, with microseconds
    from datetime import datetime
    print(datetime.now().isoformat())

    # With timezone, with microseconds
    from datetime import datetime
    from dateutil.tz import tzlocal
    print(datetime.now(tzlocal()).isoformat())

    # With timezone, without microseconds
    from datetime import datetime
    from dateutil.tz import tzlocal
    print(datetime.now(tzlocal()).replace(microsecond=0).isoformat())

    # See ISO 8601 for more information about the ISO 8601 format
    


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_10_get_an_ISO_8601_timestamp()