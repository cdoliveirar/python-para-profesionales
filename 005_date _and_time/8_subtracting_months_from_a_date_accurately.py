'''
Using the calendar module
Using the dateutils module
'''

# Using the calendar module
import calendar
from datetime import date

def monthdelta(date, delta):
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12

    if not m: m = 12
    d = min(date.day, calendar.monthrange(y, m)[1])
    return date.replace(day=d, month=m, year=y)

# Using the dateutils module
import datetime
import dateutil.relativedelta
d = datetime.datetime.strptime("2023-12-07", "%Y-%m-%d")
d2 = d - dateutil.relativedelta.relativedelta(months=1)
print(d2)




# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    next_month = monthdelta(date.today(), 1)  # suma un mes mas a la fecha actual
    print(next_month)

