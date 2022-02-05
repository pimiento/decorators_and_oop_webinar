#!/usr/bin/env python3
# wraps

from functools import wraps
def mysum(x, y):
    """This is mysum function"""
    return x + y
def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """INNER"""
        return func(*args, **kwargs)
    return inner

mysum_decorated = decorator(mysum)
print(mysum_decorated.__name__)
print(mysum_decorated.__doc__)
