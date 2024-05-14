'''
The datetime module contains three primary types of objects - date, time, and datetime.
'''
from datetime import datetime, timedelta

def function_switching_between_time_zones():
    from datetime import datetime
    from dateutil import tz
    utc = tz.tzutc()
    local = tz.tzlocal()
    utc_now = datetime.utcnow()
    # Not timezone-aware.
    print("utc_now Not timezone-aware: %s" % utc_now)
    # Timezone-aware.
    utc_now = utc_now.replace(tzinfo=utc)
    print("utc_now Timezone-aware: %s" % utc_now)
    # Converted to local time.
    local_now = utc_now.astimezone(local)
    print(local_now)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_switching_between_time_zones()