import datetime

def log_calls(log_time):
    def my_dec(func):
        def wrapper(*args, **kwargs):
            call_time=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            text_entry=f"{call_time} - function - {func.__name__} called with args={args}, kwargs={kwargs}\n"
            with open(log_time, "a") as f:
                f.write(text_entry)
            return func(*args, **kwargs)
        return wrapper
    return my_dec

@log_calls("log_time.txt")
def power(a, b):
    power=a**b
    return power

@log_calls("log_time.txt")
def great(name, greating="Hello"):
    return f"{greating}, {name}"

print(power(4,7))
print(great("Victoria"))
    