#!/usr/bin/env python3
# getter/setter/deleter

from dataclasses import dataclass
@dataclass
class A:
    __x: list
    @property
    def x(self):
        return self.__x[::]
    @x.setter
    def x(self, value):
        self.__x.append(value)
    @x.deleter
    def x(self):
        self.__x = []
a = A([])
print(a.x)
a.x = 10
print(a.x)
a.x = 100
print(a.x)
del a.x
print(a.x)
