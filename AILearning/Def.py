from timeit import timeit
from contextlib import contextmanager
def square(x):
    """Square of x."""
    return x*x


def cube(x):
    """Cube of x."""
    return x*x*x


funcs = {
    'square': square,
    'cube': cube,
}

# x = 2
# for func in sorted(funcs):
#     print func, funcs[func](x), funcs[func]


# def f(x=[]):
#     x.append(1)
#     return x


def f(x=None):
    if x is None:
        x = []
    x.append(1)
    return x


# print f()
# print f()
# print f()
# print f(x=[9, 9, 9])
# print f()
# print f()

# print map(square, range(5))


def fib1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b


# print [fib2(i) for i in range(10)]
# print [fib1(i) for i in range(10)]


class ReverseListIterator(object):
    def __init__(self, list):
        self.list = list
        self.index = len(list)

    def __iter__(self):
        return self

    def next(self):
        self.index -= 1
        if self.index >= 0:
            return self.list[self.index]
        else:
            raise StopIteration


# x = range(10)
# for i in ReverseListIterator(x):
#     print i,


def collatz(n):
    sequence = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence

# for x in collatz(7):
#     print x,


class ContextManager(object):

    def __enter__(self):
        print "Entering"

    def __exit__(self, exc_type, exc_value, traceback):
        print "Exiting"
        if exc_type is not None:
            print "Exc_type: ", exc_type
            print " Exception suppresed:", exc_value
            return True

# with ContextManager():
#     print "Inside the with statement"


@contextmanager
def my_contextmanager():
    print "Enter"
    try:
        yield
    except Exception as exc:
        print " Error: ", exc
    finally:
        print "Exit"

with my_contextmanager():
    print 4 << -1