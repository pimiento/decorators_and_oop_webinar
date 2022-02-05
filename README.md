- [Что такое декораторы](#orgf3c0796)
- [Что такое декораторы](#org6163a83)
- [Области видимости](#org49f05ab)
- [Области видимости](#orgd563f29)
- [nonlocal](#org81eeda3)
- [global](#orge4f9d00)
- [Всё понятно, но вот конкретно…](#orgafd15b0)
- [Не, всё понятно, но вот конкретно…](#orge604b22)
- [Вроде всё понятно…](#orgaa58e5a)
- [И как это понимать?](#org9cecc17)
- [Замыкания](#org5910ff4)
- [Замыкания](#org3c83bef)
- [Замыкания](#org3416f59)
- [Замыкания](#org013cb5c)
- [Декораторы и имя функции](#orgc6ecea3)
- [wraps](#org7fa2d74)
- [Декораторы с аргументами](#orga1bba03)
- [Декораторы с аргументами](#org3766d7b)
- [Декораторы с аргументами](#org4734056)
- [classmethod](#orgb884a77)
- [staticmethod](#org200daa1)
- [staticmethod](#orgac1005e)
- [Классы-декораторы](#org880f59f)
- [Класссы-декораторы и замыкания](#orgd66e962)
- [Больше про декораторы](#org6614b1c)
- [магические методы классов в Python](#org5928afb)
- [property](#org55ab6f5)
- [getter/setter/deleter](#org2e8f1cd)
- [getter/setter/deleter](#orgcd95e39)
- [Singleton](#org0d79e46)
- [Singleton](#org2bf8568)
- [Singleton](#org688f788)
- [Singleton](#org146b228)
- [Дополнительные материалы](#orga18f5b3)
- [Вопросы-ответы](#org072680d)



<a id="orgf3c0796"></a>

# Что такое декораторы

```python
def decorator(func):
    def inner(*args, **kwargs):
        print(
            "Сейчас будет выполнена "
            f"функция: {func.__name__}"
        )
        result = func(*args, **kwargs)
        print(
            f"функция {func.__name__} "
            "успешно выполнена"
        )
        return result
    return inner
```


<a id="org6163a83"></a>

# Что такое декораторы

```python

def mysum(x, y):
    print(f"x + y = {x+y}")
    return x + y

sum_decorated = decorator(mysum)
sum_decorated(6, 7)
```

    Сейчас будет выполнена функция: mysum
    x + y = 13
    функция mysum успешно выполнена


<a id="org49f05ab"></a>

# Области видимости

```python
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
```


<a id="orgd563f29"></a>

# Области видимости

```python
counter = 0
def decorator(func):
    def inner(*args, **kwargs):
        counter += 1
        result = func(*args, **kwargs)
        print(
            "Функция выполнена "
            f"{counter} раз"
        )
        return result
    return inner
```


<a id="org81eeda3"></a>

# nonlocal

```python
def decorator(func):
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        result = func(*args, **kwargs)
        print(
            "Функция выполнена "
            f"{counter} раз"
        )
        return result
    return inner
```


<a id="orge4f9d00"></a>

# global

```python
counter = 0
def decorator(func):
    def inner(*args, **kwargs):
        global counter
        counter += 1
        result = func(*args, **kwargs)
        print(
            "Функция выполнена "
            f"{counter} раз"
        )
        return result
    return inner
```


<a id="orgafd15b0"></a>

# Всё понятно, но вот конкретно…

```python

counter = {}
def decorator(func):
    counter[func.__name__] = 0
    def inner(*args, **kwargs):
        counter[func.__name__] += 1
        result = func(*args, **kwargs)
        print(counter[func.__name__])
        return result
    return inner
mysum_decorated = decorator(mysum)
mysum_decorated(2, 2)
mysum_decorated(2, 2)
mysum_decorated(3, 1)
```

    1
    2
    3


<a id="orge604b22"></a>

# Не, всё понятно, но вот конкретно…

```python

def decorator(func):
    counter = [0]
    def inner(*args, **kwargs):
        counter[0] += 1
        result = func(*args, **kwargs)
        print(counter[0])
        return result
    return inner
mysum_decorated = decorator(mysum)
mysum_decorated(2, 2)
mysum_decorated(2, 2)
mysum_decorated(3, 1)
```

    1
    2
    3


<a id="orgaa58e5a"></a>

# Вроде всё понятно…

```python
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
```


<a id="org9cecc17"></a>

# И как это понимать?

```python
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
```


<a id="org5910ff4"></a>

# Замыкания

```python
def cached(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            print("Положить в кеш")
            cache[args] = func(*args)
        else:
            print("Результат из кеша")
        return cache[args]
    return wrapper

@cached
def mysum(x, y):
    return x + y

```


<a id="org3c83bef"></a>

# Замыкания

```python

mysum(1, 2)
mysum(1, 2)
mysum(2, 3)
mysum(2, 3)
mysum(1, 2)
```

    Положить в кеш
    Результат из кеша
    Положить в кеш
    Результат из кеша
    Результат из кеша


<a id="org3416f59"></a>

# Замыкания

```python
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
```


<a id="org013cb5c"></a>

# Замыкания

```python

mysum(1, 2)
mysum(1, 2)
mysum(2, 3)
mysum(2, 3)
mysum(1, 2)
mysum.invalidate(2, 3)
```

    Положить в кеш
    Результат из кеша
    Положить в кеш
    Результат из кеша
    Результат из кеша
    Сбросить кеш
    Положить в кеш


<a id="orgc6ecea3"></a>

# Декораторы и имя функции

```python

def mysum(x,y):
    """MYSUM"""
    return x+y

mysum_decorated = decorator(mysum)
print(mysum.__name__)
print(mysum.__doc__)
print(mysum_decorated.__name__)
print(mysum_decorated.__doc__)
```

    mysum
    MYSUM
    inner
    None


<a id="org7fa2d74"></a>

# wraps

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """INNER"""
        return func(*args, **kwargs)
    return inner

mysum_decorated = decorator(mysum)
print(mysum_decorated.__name__)
print(mysum_decorated.__doc__)
```

    mysum
    This is mysum function


<a id="orga1bba03"></a>

# Декораторы с аргументами

```python

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
```


<a id="org3766d7b"></a>

# Декораторы с аргументами

```python

@benchmark()
def countdown(n):
    while n > 0:
        n -= 1

countdown(int(5e7))
```

    AVG: 2.4751


<a id="org4734056"></a>

# Декораторы с аргументами

```python

def countdown(n):
    while n > 0:
        n -= 1

countdown_decorated = \
    benchmark(5)(countdown)
countdown_decorated(int(5e7))
```

    AVG: 2.3992


<a id="orgb884a77"></a>

# classmethod

Принимает в качестве первого аргумента сам класс **cls** а не объект **self**.

```python
class MyDict:
    def __init__(self, d):
        self.data = d
    @classmethod
    def from_pairs(cls, pairs):
        return cls(dict(pairs))
pairs = (("a", 1), ("b", 2))
print(MyDict.from_pairs(pairs).data)
```

    {'a': 1, 'b': 2}


<a id="org200daa1"></a>

# staticmethod

Не привязан ни к текущему объекту **self** ни к классу **cls**.

```python
import os

class Executor:
    def __init__(self, command):
        self.command = command
    @staticmethod
    def chdir(path):
        os.chdir(path)
    def __call__(self):
        return (
            os.popen(self.command)
            .read().strip()
        )
```


<a id="orgac1005e"></a>

# staticmethod

```python

orig_path = os.getcwd()
executor = Executor("ls|wc -l")
print(os.getcwd())
print(executor())
Executor.chdir("/tmp/")
print(os.getcwd())
print(executor())
executor.chdir(orig_path)
print(os.getcwd())
```

    /home/pimiento/yap/decorators_and_oop
    28
    /tmp
    72
    /home/pimiento/yap/decorators_and_oop


<a id="org880f59f"></a>

# Классы-декораторы

```python
class Decorator:
    def __cal__(self, fn):
        def wrapper(*a, **kw):
            print("BEFORE")
            result = fn(*a, **kw)
            print("AFTER")
            return result
        return wrapper

@Decorator
def mysum(x, y):
    return x + y
```


<a id="orgd66e962"></a>

# Класссы-декораторы и замыкания

<span class="underline"><span class="underline">[пример на GitHub](https://github.com/pimiento/decorators_and_oop_webinar/blob/master/17a_class_decorator.py)</span></span>


<a id="org6614b1c"></a>

# Больше про декораторы

<span class="underline"><span class="underline">[TheDecoratorsTheyWontTellYouAbout](https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb)</span></span>


<a id="org5928afb"></a>

# магические методы классов в Python

<span class="underline"><span class="underline">[magicmethods](https://rszalski.github.io/magicmethods/)</span></span>


<a id="org55ab6f5"></a>

# property

```python

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
```

    10
    can't set attribute


<a id="org2e8f1cd"></a>

# getter/setter/deleter

```python

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
```


<a id="orgcd95e39"></a>

# getter/setter/deleter

```python

a = A([])
print(a.x)
a.x = 10
print(a.x)
a.x = 100
print(a.x)
del a.x
print(a.x)
```

    []
    [10]
    [10, 100]
    []


<a id="org0d79e46"></a>

# Singleton

```python
class Logger:
    def __init__(self):
        pass
l1 = Logger()
l2 = Logger()
print(l1 is l2)
```

    False


<a id="org2bf8568"></a>

# Singleton

```python
class Logger:
    _instance = None
    def __init__(self):
        raise RuntimeError(
            "Call new() instead"
        )
    @classmethod
    def new(cls):
        if cls._instance is None:
            cls._instance = (
                cls.__new__(cls)
            )
        return cls._instance
```


<a id="org688f788"></a>

# Singleton

```python

l1 = Logger.new()
l2 = Logger.new()
print(l1.__class__.__name__)
print(l1 is l2)
```

    Logger
    True


<a id="org146b228"></a>

# Singleton

```python
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = (
                super().__new__(cls)
            )
        return cls._instance
l1 = Logger()
l2 = Logger()
print(l1.__class__.__name__)
print(l1 is l2)
```

    Logger
    True


<a id="orga18f5b3"></a>

# Дополнительные материалы

<span class="underline"><span class="underline">[Паттерны проектирования на Python](https://python-patterns.guide/)</span></span>
<span class="underline"><span class="underline">[Head First](https://www.amazon.com/Head-First-Design-Patterns-Brain-Friendly/dp/0596007124)</span></span>


<a id="org072680d"></a>

# Вопросы-ответы

![img](/home/pimiento/yap/questions.jpg)
