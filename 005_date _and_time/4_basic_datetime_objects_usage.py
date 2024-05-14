'''
The datetime module contains three primary types of objects - date, time, and datetime.
'''
from datetime import datetime, timedelta

def function_basic_datetime_objects_usage():
    import datetime
    # Date object
    today = datetime.date.today()   # 2017-01-01
    print("Today: %s" % today)
    new_year = datetime.date(2025, 0o1, 0o1)  # datetime.date(2017, 1, 1)
    print(new_year)
    # Time object
    noon = datetime.time(12, 0, 0)  # datetime.time(12, 0)
    # Current datetime
    now = datetime.datetime.now()   # 2023-12-06 19:14_12.645608
    print(now)

    # ----
    noon = datetime.time(12, 0, 0)  # datetime.time(12, 0)
    print(noon)

    # Datetime object
    millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)  # datetime.datetime(2000, 1, 1, 0, 0)

    print('Time since the millenium at midnight: ', datetime.datetime(today.year, today.month, today.day) - millenium_turn)

    # Or this
    print('Time since the millenium at noon: ', datetime.datetime.combine(today, noon) - millenium_turn)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_basic_datetime_objects_usage()