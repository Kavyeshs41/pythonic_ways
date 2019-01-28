from pymongo import MongoClient

db = MongoClient("127.0.0.1:27017")["hire_scikey"]

for data in db.candidates.find({"skills" : {"$exists" : True}}):
    # print(data["skills"])
    skillDataObject = data["skills"]
    for skillData in skillDataObject:
        print(skillData)
    # try:
    #     for skill in data["skills"].get("primary"):
    #         try:
    #
    #         except KeyError:
    #             continue
    # except KeyError:
    #     continue
