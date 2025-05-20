import functools


def retry(exception_type, n):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(n):
                try:
                    return func(*args, **kwargs)
                except exception_type as e:
                    last_exception = e
                    if attempt == n - 1:
                        raise
            raise last_exception

        return wrapper

    return decorator_retry
