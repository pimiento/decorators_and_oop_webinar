# &#1057;&#1086;&#1076;&#1077;&#1088;&#1078;&#1072;&#1085;&#1080;&#1077;

1.  [Что такое декораторы](#org79e7c85)
2.  [Что такое декораторы](#org5f0ac46)
3.  [Области видимости](#org2b92ec8)
4.  [Области видимости](#org28b57b2)
5.  [nonlocal](#orgb2273d2)
6.  [global](#orgd50fc74)
7.  [Всё понятно, но вот конкретно…](#orgcbad196)
8.  [Не, всё понятно, но вот конкретно…](#org8a96ffd)
9.  [Вроде всё понятно…](#org79f4b0c)
10. [И как это понимать?](#orgb4a61c0)
11. [Замыкания](#org83a63b7)
12. [Замыкания](#orga8b7e91)
13. [Замыкания](#orga0c4f7d)
14. [Замыкания](#org91caa59)
15. [Декораторы и имя функции](#org4c23fef)
16. [wraps](#org3ade7a0)
17. [Декораторы с аргументами](#orgb3e0e03)
18. [Декораторы с аргументами](#org8169056)
19. [Декораторы с аргументами](#org95cd7aa)
20. [classmethod](#org3d7e762)
21. [staticmethod](#org4df6fc8)
22. [staticmethod](#orgbba65ca)
23. [Классы-декораторы](#orgabe3ee4)
24. [Класссы-декораторы и замыкания](#org39c9873)
25. [Больше про декораторы](#org08064ff)
26. [магические методы классов в Python](#org8bfd48f)
27. [property](#org5c4d1cb)
28. [getter/setter/deleter](#org9a25abd)
29. [getter/setter/deleter](#org81c8844)
30. [Singleton](#orgb53238e)
31. [Singleton](#org75ab66c)
32. [Singleton](#orgc5a8803)
33. [Singleton](#orgcab8e04)
34. [Дополнительные материалы](#orgd1fd5ff)
35. [Вопросы-ответы](#orgbffe528)



<a id="org79e7c85"></a>

# Что такое декораторы

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


<a id="org5f0ac46"></a>

# Что такое декораторы


    def mysum(x, y):
        print(f"x + y = {x+y}")
        return x + y

    sum_decorated = decorator(mysum)
    sum_decorated(6, 7)

    Сейчас будет выполнена функция: mysum
    x + y = 13
    функция mysum успешно выполнена


<a id="org2b92ec8"></a>

# Области видимости

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


<a id="org28b57b2"></a>

# Области видимости

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


<a id="orgb2273d2"></a>

# nonlocal

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


<a id="orgd50fc74"></a>

# global

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


<a id="orgcbad196"></a>

# Всё понятно, но вот конкретно…


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

    1
    2
    3


<a id="org8a96ffd"></a>

# Не, всё понятно, но вот конкретно…


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

    1
    2
    3


<a id="org79f4b0c"></a>

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


<a id="orgb4a61c0"></a>

# И как это понимать?

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

    0 1


<a id="org83a63b7"></a>

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
        return wrapper

    @cached
    def mysum(x, y):
        return x + y


<a id="orga8b7e91"></a>

# Замыкания


    mysum(1, 2)
    mysum(1, 2)
    mysum(2, 3)
    mysum(2, 3)
    mysum(1, 2)

    Положить в кеш
    Результат из кеша
    Положить в кеш
    Результат из кеша
    Результат из кеша


<a id="orga0c4f7d"></a>

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


<a id="org91caa59"></a>

# Замыкания


    mysum(1, 2)
    mysum(1, 2)
    mysum(2, 3)
    mysum(2, 3)
    mysum(1, 2)
    mysum.invalidate(2, 3)

    Положить в кеш
    Результат из кеша
    Положить в кеш
    Результат из кеша
    Результат из кеша
    Сбросить кеш
    Положить в кеш


<a id="org4c23fef"></a>

# Декораторы и имя функции


    def mysum(x,y):
        """MYSUM"""
        return x+y

    mysum_decorated = decorator(mysum)
    print(mysum.__name__)
    print(mysum.__doc__)
    print(mysum_decorated.__name__)
    print(mysum_decorated.__doc__)

    mysum
    MYSUM
    inner
    None


<a id="org3ade7a0"></a>

# wraps

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

    mysum
    This is mysum function


<a id="orgb3e0e03"></a>

# Декораторы с аргументами


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


<a id="org8169056"></a>

# Декораторы с аргументами


    @benchmark()
    def countdown(n):
        while n > 0:
            n -= 1

    countdown(int(5e7))

    AVG: 2.3782


<a id="org95cd7aa"></a>

# Декораторы с аргументами


    def countdown(n):
        while n > 0:
            n -= 1

    countdown_decorated = \
        benchmark(5)(countdown)
    countdown_decorated(int(5e7))

    AVG: 2.3841


<a id="org3d7e762"></a>

# classmethod

Принимает в качестве первого аргумента сам класс **cls** а не объект **self**.

    class MyDict:
        def __init__(self, d):
            self.data = d
        @classmethod
        def from_pairs(cls, pairs):
            return cls(dict(pairs))
    pairs = (("a", 1), ("b", 2))
    print(MyDict.from_pairs(pairs).data)

    {'a': 1, 'b': 2}


<a id="org4df6fc8"></a>

# staticmethod

Не привязан ни к текущему объекту **self** ни к классу **cls**.

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


<a id="orgbba65ca"></a>

# staticmethod


    orig_path = os.getcwd()
    executor = Executor("ls|wc -l")
    print(os.getcwd())
    print(executor())
    Executor.chdir("/tmp/")
    print(os.getcwd())
    print(executor())
    executor.chdir(orig_path)
    print(os.getcwd())

    /home/pimiento/yap/decorators_and_oop
    28
    /tmp
    72
    /home/pimiento/yap/decorators_and_oop


<a id="orgabe3ee4"></a>

# Классы-декораторы

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


<a id="org39c9873"></a>

# Класссы-декораторы и замыкания

<span class="underline"><span class="underline">[пример на GitHub](https://github.com/pimiento/decorators_and_oop_webinar/blob/master/17a_class_decorator.py)</span></span>


<a id="org08064ff"></a>

# Больше про декораторы

<span class="underline"><span class="underline">[TheDecoratorsTheyWontTellYouAbout](https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb)</span></span>


<a id="org8bfd48f"></a>

# магические методы классов в Python

<span class="underline"><span class="underline">[magicmethods](https://rszalski.github.io/magicmethods/)</span></span>


<a id="org5c4d1cb"></a>

# property


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

    10
    can't set attribute


<a id="org9a25abd"></a>

# getter/setter/deleter


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


<a id="org81c8844"></a>

# getter/setter/deleter


    a = A([])
    print(a.x)
    a.x = 10
    print(a.x)
    a.x = 100
    print(a.x)
    del a.x
    print(a.x)

    []
    [10]
    [10, 100]
    []


<a id="orgb53238e"></a>

# Singleton

    class Logger:
        def __init__(self):
            pass
    l1 = Logger()
    l2 = Logger()
    print(l1 is l2)

    False


<a id="org75ab66c"></a>

# Singleton

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


<a id="orgc5a8803"></a>

# Singleton


    l1 = Logger.new()
    l2 = Logger.new()
    print(l1.__class__.__name__)
    print(l1 is l2)

    Logger
    True


<a id="orgcab8e04"></a>

# Singleton

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

    Logger
    True


<a id="orgd1fd5ff"></a>

# Дополнительные материалы

<span class="underline"><span class="underline">[Паттерны проектирования на Python](https://python-patterns.guide/)</span></span>
<span class="underline"><span class="underline">[Head First](https://www.amazon.com/Head-First-Design-Patterns-Brain-Friendly/dp/0596007124)</span></span>


<a id="orgbffe528"></a>

# Вопросы-ответы

![img](/home/pimiento/yap/questions.jpg)
