'''
Las fechas no existen de forma aislada. Es común que necesites encontrar la cantidad de tiempo entre fechas o
determinar cuál será la fecha de mañana. Esto se puede lograr usando objetos timedelta.
'''
from datetime import datetime, timedelta

def function_simple_date_arithmetic():
    import datetime
    today = datetime.date.today()
    print('Today:', today)
    yesterday = today - datetime.timedelta(days=1)
    print('Yesterday:', yesterday)
    tomorrow = today + datetime.timedelta(days=1)
    print('Tomorrow:', tomorrow)
    print('Time between tomorrow and yesterday:', tomorrow - yesterday)



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_simple_date_arithmetic()