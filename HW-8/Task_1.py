import time
import functools

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        time_of_work = (end - start) * 1000
        print(f"It took {time_of_work:.2f} ms")
        return result
    return wrapper

