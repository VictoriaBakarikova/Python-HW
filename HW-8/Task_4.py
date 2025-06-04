import threading
import time
from collections import deque
from functools import wraps


class RateLimitException(Exception):
    pass


def rate_limit(max_calls, period):
    def decorator(func):
        lock = threading.Lock()
        call_times = deque()

        @wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                now = time.monotonic()
                while call_times and now - call_times[0] > period:
                    call_times.popleft()
                if len(call_times) >= max_calls:
                    raise RateLimitException(
                        f"Сall limit exceeded:"
                        f" allowed {max_calls} in {period} sec"
                    )
                call_times.append(now)
            return func(*args, **kwargs)

        return wrapper()

    return decorator
