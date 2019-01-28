valueDict = [{"name":"Sandeep","age":"21"},{"name":"Alay","age":"20"},{"name":"Abhi","age":"21"},{"name":"Abhishek","age":"23"},{"name":"Apurva","age":"23"},{"name":"Kunal","age":"19"},{"name":"Shrey","age":"18"}]

#print(valueDict)

def clean(x):

    b = [a['age'] for a in x]
    b = list(set(b))
    name = [a['name'] for a in x]

    newDict = {}
    if x['age'] in newDict:
        print("xy")
    else:
        newDict['age'] = x['name']

    print(newDict)
    return 0;
    # age = list(set(b))
    # for i in age,name:
print(clean(valueDict))