def cache(func):
    cache_dict={}
    
    def wrapper(*args, **kwargs):
        key=(args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Cash result: ")
            return cache_dict[key]
        add_dict=func(*args, **kwargs)
        cache_dict[key]=add_dict
        return add_dict
    return wrapper

@cache
def add(x, y):
    return x**y

print(add(4, 7))
print(add(4, 6))
print(add(4, 5))
print(add(4, 7))
    

