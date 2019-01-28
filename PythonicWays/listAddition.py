import functools


def add(a, b):
    return a + b


numArr = [1, 2, 3]


x = functools.reduce(add, numArr)
print(x);