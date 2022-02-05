#!/usr/bin/env python3
# global

counter = 0
def decorator(func):
    def inner(*args, **kwargs):
        global counter
        counter += 1
        result = func(*args, **kwargs)
        print(
            "Функция выполнена "
            f"{counter} раз"
        )
        return result
    return inner

@decorator
def mysum(x, y):
    return x + y

mysum(1, 2)

@decorator
def mymul(x, y):
    return x * y

mymul(1, 2)
