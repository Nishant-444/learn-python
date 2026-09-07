import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result

    return wrapper


@timer
def example_function(n):
    time.sleep(n)


# example_function(2)
# #########################################################


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


def debug(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# #########################################################
def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(5)
    return a + b


# print(long_running_function(2, 3))
# print(long_running_function(3, 3))
