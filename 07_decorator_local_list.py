#!/usr/bin/env python3
# Не, всё понятно, но вот конкретно…

def mysum(x, y):
    """This is mysum function"""
    return x + y
def decorator(func):
    counter = [0]
    def inner(*args, **kwargs):
        counter[0] += 1
        result = func(*args, **kwargs)
        print(counter[0])
        return result
    return inner
mysum_decorated = decorator(mysum)
mysum_decorated(2, 2)
mysum_decorated(2, 2)
mysum_decorated(3, 1)
