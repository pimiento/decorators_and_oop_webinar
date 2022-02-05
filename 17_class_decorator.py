#!/usr/bin/env python3
# Классы-декораторы

class Decorator:
    def __cal__(self, fn):
        def wrapper(*a, **kw):
            print("BEFORE")
            result = fn(*a, **kw)
            print("AFTER")
            return result
        return wrapper

@Decorator
def mysum(x, y):
    return x + y
