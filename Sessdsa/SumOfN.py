import time
import random
def sum_of_n_2(n):
    start = time.time()
    print(start)
    the_sum = 0
    for i in range(1, n+1):
        the_sum += i
    end = time.time()
    print(end)
    return the_sum, end - start

def sum_of_n_3(n):
    start = time.time()
    the_sum = (n * (n + 1))/2
    end = time.time()
    return the_sum, end - start

def fin_min_1():
    list = []
    for i in range(1000000):
        list.append(random.randint(1, 100))
    # print(list)
    min = 100
    start = time.time()
    for i in list:
        if(i < min):
            min = i
    end = time.time()
    return min, end - start

def fin_min_2():
    list = []
    for i in range(1000000):
        list.append(random.randint(1, 100))
    start = time.time()
    list.sort()
    min = list[0]
    end = time.time()
    return min, end - start

print(fin_min_1())
# for i in range(5):
#     print('Sum is %d required %10.7f seconds' %sum_of_n_2(100000000))