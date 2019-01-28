from functools import reduce

arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101]


add_10 = (list(map(lambda x: x + 10, arr)))
add_20 = (list(map(lambda x: x + 20, arr)))

print(add_10)
print(add_20)

odd = (list(filter(lambda x: x % 2 == 0, arr)))
even = (list(filter(lambda x: x % 2 == 1, arr)))

print(odd)
print(even)

addition = (reduce(lambda x, y: x + y, arr))

print(addition)

ele = (arr[-1])

print(ele)
