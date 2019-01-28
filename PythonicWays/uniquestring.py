from collections import defaultdict

a = list(input("Enter a string"))
d = defaultdict(lambda: 0)

for i in a:
    d[i] += 1
    if d[i] >1:
        print("String has non unique character = " + i)

print(d)



