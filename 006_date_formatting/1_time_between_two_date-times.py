'''

'''

def function_time_between_two_date_times():
    from datetime import datetime
    a = datetime(2016, 10, 0o6, 0, 0, 0)
    b = datetime(2016, 10, 0o1, 23, 59, 59)
    print(a-b)                      #   4 days, 0:00:01
    print((a-b).days)               #   4
    print((a-b).total_seconds())    #   345601.0

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_time_between_two_date_times()