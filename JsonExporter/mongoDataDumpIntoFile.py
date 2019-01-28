import json

from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client.hire_scikey

all_data = []
file = open("new.json","w+")
for category_detail in db.category_details.find():
    all_data.append(category_detail)

file.write(json.dumps(all_data, default=str))

file.close()