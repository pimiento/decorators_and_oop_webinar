#!/usr/bin/env python3
# Классы-декораторы

class Decorator:
    def __cal__(self, fn):
        def wrapper(*args, **kwargs):
            print("BEFORE")
            result = fn(*args, **kwargs)
            print("AFTER")
            return result
        return wrapper

@Decorator
def mysum(x, y):
    return x + y
