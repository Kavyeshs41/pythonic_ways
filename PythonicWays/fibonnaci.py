from functools import partial


def fibonnaci(a):
    x = [0, 1]
    for i in range(a-2):
        x.append(x[-1]+x[-2])
    return x

print(fibonnaci(8))