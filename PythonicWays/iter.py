zoro = "roronoa"

a = iter(zoro)

def abc(x):
    try:
        while True:
            print(x.__next__());
    except StopIteration:
        print('Exception  - Over!')
