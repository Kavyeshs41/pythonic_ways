from pymongo import MongoClient
import requests
import json
# from bson import json_util, ObjectId

client = MongoClient("127.0.0.1", 27017)

URL_encrypt_dev = "http://10.0.4.4:8108/crypto/v1/encrypt?env=&orgname=hire&domain_name=scikey"

db = client.hire_scikey
collection = db.marketing_campaign_data

res = collection.find({
                "recipient_contact": {"$exists" : True},
                "recipient_email": {"$exists" : True}
            },
            {"_id": 1, "recipient_contact": 1, "recipient_email": 1})

detail_list = []
for doc in res:
    detail_list.append(doc)

email_list = []
phone_list = []
for i in range(detail_list.__len__()):
    email_decr = detail_list[i]['recipient_email']
    phone_decr = detail_list[i]['recipient_contact']

    email_list.append({
        "resources": {
            "email": email_decr
        }
    })

    phone_list.append({
        "resources": {
            "email": phone_decr
        }
    })

# print(json.dumps(email_list))
email_result = requests.post(url=URL_encrypt_dev, data=json.dumps(email_list),
                           headers={"Content-Type": "application/json"})
phone_result = requests.post(url=URL_encrypt_dev, data=json.dumps(phone_list),
                           headers={"Content-Type": "application/json"})

for x in range(email_result)
    temp_dict = {"email": email_result.json()['data'][0]['resources']['email']}
print(temp_dict)