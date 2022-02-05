#!/usr/bin/env python3
# Декораторы и имя функции

def decorator(func):
    def inner(*args, **kwargs):
        print(
            "Сейчас будет выполнена "
            f"функция: {func.__name__}"
        )
        result = func(*args, **kwargs)
        print(
            f"функция {func.__name__} "
            "успешно выполнена"
        )
        return result
    return inner
def mysum(x,y):
    """MYSUM"""
    return x+y

mysum_decorated = decorator(mysum)
print(mysum.__name__)
print(mysum.__doc__)
print(mysum_decorated.__name__)
print(mysum_decorated.__doc__)
