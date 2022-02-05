#!/usr/bin/env python3
def mysum(x, y):
    """This is mysum function"""
    return x + y
counter = {}
def decorator(func):
    counter[func.__name__] = 0
    def inner(*args, **kwargs):
        counter[func.__name__] += 1
        result = func(*args, **kwargs)
        print(counter[func.__name__])
        return result
    return inner
mysum_decorated = decorator(mysum)
mysum_decorated(2, 2)
mysum_decorated(2, 2)
mysum_decorated(3, 1)
