# &#1057;&#1086;&#1076;&#1077;&#1088;&#1078;&#1072;&#1085;&#1080;&#1077;

1.  [Что такое декораторы](#orge226c4e)
2.  [Что такое декораторы](#org8599036)
3.  [Области видимости](#orga19491b)
4.  [Области видимости](#org5c12cd4)
5.  [nonlocal](#orgdfca4a6)
6.  [global](#org98e94e6)
7.  [Всё понятно, но вот конкретно…](#org6cad248)
8.  [Не, всё понятно, но вот конкретно…](#org65b858d)
9.  [Вроде всё понятно…](#org4bd9961)
10. [И как это понимать?](#orgd46c837)
11. [Замыкания](#org5b463bd)
12. [Замыкания](#orgfaa08ce)
13. [Замыкания](#org71ec6a7)
14. [Замыкания](#org569d469)
15. [Декораторы и имя функции](#org2223ff1)
16. [wraps](#org6ded818)
17. [Декораторы с аргументами](#org4f3f201)
18. [Декораторы с аргументами](#org2c7c4a5)
19. [Декораторы с аргументами](#orga858f66)
20. [classmethod](#org4f45e3c)
21. [staticmethod](#org1f9899d)
22. [staticmethod](#org5723d01)
23. [Классы-декораторы](#org1b81120)
24. [Класссы-декораторы и замыкания](#orgf5328da)
25. [Больше про декораторы](#orgf0a47f3)
26. [магические методы классов в Python](#org357ff93)
27. [property](#orgb06c8da)
28. [getter/setter/deleter](#org75af011)
29. [getter/setter/deleter](#org5272ce2)
30. [Singleton](#orge7138da)
31. [Singleton](#orga7ccb89)
32. [Singleton](#orgdc3be1e)
33. [Дополнительные материалы](#org61358b4)
34. [Вопросы](#org9afa093)



<a id="orge226c4e"></a>

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


<a id="org8599036"></a>

# Что такое декораторы


    def mysum(x, y):
        print(f"x + y = {x+y}")
        return x + y

    sum_decorated = decorator(mysum)
    sum_decorated(6, 7)

    Сейчас будет выполнена функция: mysum
    x + y = 13
    функция mysum успешно выполнена


<a id="orga19491b"></a>

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


<a id="org5c12cd4"></a>

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


<a id="orgdfca4a6"></a>

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


<a id="org98e94e6"></a>

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


<a id="org6cad248"></a>

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


<a id="org65b858d"></a>

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


<a id="org4bd9961"></a>

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


<a id="orgd46c837"></a>

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


<a id="org5b463bd"></a>

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


<a id="orgfaa08ce"></a>

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


<a id="org71ec6a7"></a>

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


<a id="org569d469"></a>

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


<a id="org2223ff1"></a>

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


<a id="org6ded818"></a>

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


<a id="org4f3f201"></a>

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


<a id="org2c7c4a5"></a>

# Декораторы с аргументами


    @benchmark()
    def countdown(n):
        while n > 0:
            n -= 1

    countdown(int(5e7))

    AVG: 2.4195


<a id="orga858f66"></a>

# Декораторы с аргументами


    def countdown(n):
        while n > 0:
            n -= 1

    countdown_decorated = \
        benchmark(5)(countdown)
    countdown_decorated(int(5e7))

    AVG: 2.3785


<a id="org4f45e3c"></a>

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


<a id="org1f9899d"></a>

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


<a id="org5723d01"></a>

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
    24
    /tmp
    72
    /home/pimiento/yap/decorators_and_oop


<a id="org1b81120"></a>

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


<a id="orgf5328da"></a>

# Класссы-декораторы и замыкания

<span class="underline"><span class="underline">[пример на GitHub](https://github.com/pimiento/decorators_and_oop_webinar/blob/master/17a_class_decorator.py)</span></span>


<a id="orgf0a47f3"></a>

# Больше про декораторы

<span class="underline"><span class="underline">[TheDecoratorsTheyWontTellYouAbout](https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb)</span></span>


<a id="org357ff93"></a>

# магические методы классов в Python

<span class="underline"><span class="underline">[magicmethods](https://rszalski.github.io/magicmethods/)</span></span>


<a id="orgb06c8da"></a>

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


<a id="org75af011"></a>

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


<a id="org5272ce2"></a>

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


<a id="orge7138da"></a>

# Singleton

    class Logger:
        def __init__(self):
            pass
    l1 = Logger()
    l2 = Logger()
    print(l1 is l2)

    False


<a id="orga7ccb89"></a>

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

    Logger
    True


<a id="orgdc3be1e"></a>

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

    Logger
    True


<a id="org61358b4"></a>

# Дополнительные материалы

<span class="underline"><span class="underline">[Паттерны проектирования на Python](https://python-patterns.guide/)</span></span>
<span class="underline"><span class="underline">[Head First](https://www.amazon.com/Head-First-Design-Patterns-Brain-Friendly/dp/0596007124)</span></span>


<a id="org9afa093"></a>

# Вопросы
