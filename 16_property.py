#!/usr/bin/env python3
from dataclasses import dataclass
@dataclass
class A:
    __x: int
    @property
    def x(self):
        return self.__x
a = A(10)
print(a.x)
try:
    a.x = 100
except Exception as e:
    print(e)
