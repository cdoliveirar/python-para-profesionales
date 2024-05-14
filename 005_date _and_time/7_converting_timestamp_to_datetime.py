'''
The datetime module can convert a POSIX timestamp to a ITC datetime object.
'''


def function_timestamp_to_datetime():
    import time
    from datetime import datetime
    seconds_since_epoch = time.time()   # 1469182681.709
    print(seconds_since_epoch)
    utc_date = datetime.utcfromtimestamp(seconds_since_epoch)
    print(utc_date)



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_timestamp_to_datetime()