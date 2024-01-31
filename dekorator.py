from datetime import datetime
import time


# Funkcja wywołana między 6 a 24
def check_hour(func):
    def wrapper(*args, **kwargs):
        if 6 <= datetime.now().hour < 24:
            func(*args, **kwargs)
        else:
            print("Sorry, try again later!")
    return wrapper


@check_hour
def launch():
    print('Launching application...')


launch()


# # Obliczanie sumy wszystkich kolejnych liczb dlla podanej liczby n
# # Obliczanie jak długo działa funkcja dla danej liczby n.
def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper


@execution_time_decorator
def calculate_sum(n):
    return sum(range(1, n+1))


result = calculate_sum(123456789)
print("Sum:", result)
