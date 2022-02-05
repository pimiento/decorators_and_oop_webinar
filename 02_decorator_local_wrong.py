#!/usr/bin/env python3
# Области видимости

def decorator(func):
    counter = 0
    def inner(*args, **kwargs):
        counter += 1
        result = func(*args, **kwargs)
        print(
            "Функция выполнена "
            f"{counter} раз"
        )
        return result
    return inner
