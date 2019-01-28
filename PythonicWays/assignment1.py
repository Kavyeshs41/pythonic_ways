import itertools
print("----Help Jack Sleep----\n")
user_input = input("Value Please!! it will help him sleep : =")


if user_input.isdigit() == False:
    print("You have cheated by entering a character")
    exit()

arrlist = list(user_input)  # converts input into a list

perfectList = ['1', '2','3','4','5','6','7','8','9']

arrlist1 = list(set(arrlist))

arrlist1.sort()
print(arrlist1)

if arrlist1 == perfectList:
    print("Thanks jack is asleep")
    exit()

for i in range(2, 100):
    y = str(int(user_input))
    x = list(set(str(i*int(user_input))))
    print(x, "thi is list")
    _ = x + list(str(i*int(y)))
    print(_, "finallist")
    if _ != perfectList:
        print("in if")
        _ = list(set(str(i*int(user_input))))
        set(_)
    elif _ == perfectList:
        print(i, "thi is iterable")
        print("jack is asleep")
    else:
        print("insomania")
