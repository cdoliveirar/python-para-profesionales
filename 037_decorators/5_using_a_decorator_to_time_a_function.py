'''
Usar un decorador para cronometrar una función
'''
import time


def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('Runtime took {0} seconds'.format(t2 - t1))
        return f
    return inner

@timer
def example_function():
  return "Hello World!"

print(example_function())

