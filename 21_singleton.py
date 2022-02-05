#!/usr/bin/env python3
# Singleton

class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
l1 = Logger()
l2 = Logger()
print(l1.__class__.__name__)
print(l1 is l2)
