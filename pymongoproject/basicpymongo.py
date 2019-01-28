from pymongo import MongoClient

client = MongoClient()

x = client.database_names()

for i in x:
    print(i)