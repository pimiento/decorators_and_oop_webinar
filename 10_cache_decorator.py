#!/usr/bin/env python3
# Замыкания

def cached(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            print("Положить в кеш")
            cache[args] = func(*args)
        else:
            print("Результат из кеша")
        return cache[args]
    def invalidate(*args):
        print("Сбросить кеш")
        del cache[args]
        return wrapper(*args)
    wrapper.invalidate = invalidate
    return wrapper

@cached
def mysum(x, y):
    return x + y
mysum(1, 2)
mysum(1, 2)
mysum(2, 3)
mysum(2, 3)
mysum(1, 2)
mysum.invalidate(2, 3)
