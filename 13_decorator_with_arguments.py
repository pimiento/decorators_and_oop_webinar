#!/usr/bin/env python3
# Декораторы с аргументами

import time
def benchmark(iters=3):
    def decorator(func):
        def wrapper(*a, **k):
            total = 0
            for i in range(iters):
                start = time.time()
                result = func(*a, **k)
                end = time.time()
                total += (end - start)
            print("AVG: "
                f"{total/iters:.4f}")
            return result
        return wrapper
    return decorator
@benchmark()
def countdown(n):
    while n > 0:
        n -= 1

countdown(int(5e7))
