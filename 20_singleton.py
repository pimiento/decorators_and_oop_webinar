#!/usr/bin/env python3
# Singleton

class Logger:
    _instance = None
    def __init__(self):
        raise RuntimeError("Call new() instead")
    @classmethod
    def new(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance
l1 = Logger.new()
l2 = Logger.new()
print(l1.__class__.__name__)
print(l1 is l2)
