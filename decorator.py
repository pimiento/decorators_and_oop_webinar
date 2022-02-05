#!/usr/bin/env python3
# Что такое декораторы

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
def mysum(x, y):
    print(f"x + y = {x+y}")
    return x + y

sum_decorated = decorator(mysum)
sum_decorated(6, 7)
