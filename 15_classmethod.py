#!/usr/bin/env python3
# classmethod
#   Принимает в качестве первого аргумента сам класс *cls* а не объект *self*.

class MyDict:
    def __init__(self, d):
        self.data = d
    @classmethod
    def from_pairs(cls, pairs):
        return cls(dict(pairs))
pairs = (("a", 1), ("b", 2))
print(MyDict.from_pairs(pairs).data)
