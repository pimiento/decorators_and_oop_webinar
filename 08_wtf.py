#!/usr/bin/env python3
# Вроде всё понятно…

x = 0
y = 0
def f():
    x = 1
    y = 1
    class C:
        # что будет напечатано?
        print(x, y)
        x = 2
f()
