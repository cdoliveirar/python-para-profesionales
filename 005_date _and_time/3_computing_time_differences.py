'''
El módulo timedelta resulta útil para calcular diferencias entre tiempos:
'''
from datetime import datetime, timedelta

def function_computing_time_differences():

    now = datetime.now()
    print("now: %s" % now)

    then = datetime(2016, 5, 23)
    print("then: %s" % then)

    delta = now - then
    print(delta)
    print(delta.days)
    print(delta.seconds)


# n day's after date:
def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
    date_n_days_after = datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)

# n day's before date:
def get_n_days_before_date(date_format="%d %B %Y", days_before=120):
    date_n_days_ago = datetime.now() - timedelta(days=days_before)
    return date_n_days_ago.strftime(date_format)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_computing_time_differences()
    # Sumar dias al dia actual
    sumar_dias = get_n_days_after_date("%d %B %Y", 2)
    print(sumar_dias)
    # Restar días al día actual
    restar_dias = get_n_days_before_date("%d %B %Y", 2)
    print(restar_dias)