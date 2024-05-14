'''
Sometimes you want to iterate over a range of dates from a start date to some end date. You can do it using
datetime library and timedelta object:
'''


def function_fuzzy_datetime_parsing():
    import datetime
    # The size of each step in days
    day_delta = datetime.timedelta(days=1)
    print(day_delta)
    start_date = datetime.date.today()
    print(start_date)
    end_date = start_date + 7 * day_delta
    print(end_date)
    print("---")
    for i in range((end_date - start_date).days):
        print(start_date + i*day_delta)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_fuzzy_datetime_parsing()