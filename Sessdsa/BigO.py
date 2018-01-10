import timeit

#number = 10000时
#concat  6.476135585474718 milliseconds
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

#concat  1.3533645657979827 milliseconds
def test2():
    l = []
    for i in range(1000):
        l.append(i)

#concat  1.339570540681778 milliseconds
def test3():
    l = [i for i in range(1000)]

#concat  1.352745017697848 milliseconds
def test4():
    l = list(range(1000))

t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000000), "milliseconds")

# t2 = timeit.Timer("test2()", "from __main__ import test2")
# print("concat ", t2.timeit(number=1000000), "milliseconds")

# t3 = timeit.Timer("test3()", "from __main__ import test3")
# print("concat ", t3.timeit(number=1000000), "milliseconds")

# t4 = timeit.Timer("test4()", "from __main__ import test4")
# print("concat ", t4.timeit(number=1000000), "milliseconds")