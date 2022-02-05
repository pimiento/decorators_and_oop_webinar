#!/usr/bin/env python3
# Класссы-декораторы и замыкания

from functools import wraps


class Cache:
    def __init__(self, n=3):
        self._n = n
        self.__cache = {}
        self.__wrapper = None

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args):
            if args in self.__cache and self.__cache[args]["count"] > self._n:
                print("Сброс по счётчику")
                del self.__cache[args]
            elif args in self.__cache:
                self.__cache[args]["count"] += 1
                print("Значение из кеша")
                return self.__cache[args]["result"]
            self.__cache[args] = {
                "result": func(*args),
                "count": 1
            }
            print("Записали в кеш")
            return self.__cache[args]["result"]
        self.__wrapper = wrapper
        self.__wrapper.invalidate = self.invalidate
        return self.__wrapper

    def invalidate(self, *args):
        if len(args) == 0:
            print("Сбросить весь кеш")
            self.__cache = {}
        else:
            print("Сбросить кеш для аргументов")
            del self.__cache[args]
            return self.__wrapper(*args)

@Cache(5)
def mysum(x, y):
    return x + y

print(mysum(1, 2))
print(mysum(1, 2))
print(mysum.invalidate(1, 2))
print(mysum(1, 2))
print(mysum(1, 2))
print(mysum(1, 2))
print(mysum(1, 2))
print(mysum.invalidate())
