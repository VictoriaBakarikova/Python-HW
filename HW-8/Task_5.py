import functools
import time
import warnings


def warn_if_slow(_func=None, *, threshold=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            if elapsed_time > threshold:
                warnings.warn(
                    f"Warning: {func.__name__} "
                    f"function took {elapsed_time:.2f} seconds.",
                    RuntimeWarning
                )
            return result
        return wrapper
    if _func is None:
        return decorator
    else:
        return decorator(_func)
