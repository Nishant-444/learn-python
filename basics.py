# ########################################################
# lambda function
def add(a, b):
    return a + b


result = add(5, 3)
# print(result)

cube = lambda x: x**3
# print(cube(3))


# ########################################################
# function with *args
def sum_all(*args):
    print(args)
    for i in args:
        print(i)
    return "sum: " + str(sum(args))


# print(sum_all(1, 2))
# print(sum_all(1, 2, 3, 4, 5))


# ########################################################
# function with **kwargs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print_kwargs(name="Nishant", power="mind", enemy="jack")


# ########################################################
# yield & generator function with yield
def even_generator(limit):
    # list = []
    for i in range(2, limit + 1, 2):
        yield i
        # list.append(i)
    # return list


# print(even_generator(10))
# for num in even_generator(10):
#     print(num)


# ########################################################
# recursive function


def factorial(num: int):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


# maximum recursion depth bydefault = 1000, can be changed with sys import
# print(factorial(1000))


# ########################################################
# scopes
username = "nishant4712"


def func():
    username = "nishant"
    print(username)


# print(username)
# func()

x = 99
y = 1


def func2(y):
    z = x + y
    return z


# print(func2(10))

# ########################################################
# global keyword


def func3():
    global x
    x = 12
    print(x)


# print(func3())


# ########################################################
