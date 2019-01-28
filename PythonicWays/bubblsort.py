
cnt = input("How many elements you want to enter? = ")

if cnt.isdigit() == False:
    print("You have cheated by entering a character")
    exit()

a = []
for i in range(int(cnt)):
    x = int(input("Enter Element  = "))
    a.append(x)

print(a)

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j+1] < a[j]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
