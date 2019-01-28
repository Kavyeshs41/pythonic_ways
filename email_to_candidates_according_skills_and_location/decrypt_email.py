import pandas as pd
from pymongo import MongoClient
import requests
import json

client = MongoClient("10.0.5.7", 27017)

URL_decrypt_dev = "http://10.0.4.4/crypto/v1/decrypt?env=dev&orgname=hire&domain_name=scikey"

db = client.hire_scikey
collection = db.candidates

main_arr = []

pipeline = [
    {
        "$match" : {
            "email_verified" : False,
            "contact_number_verified" : False,
            "verifiers" : {"$exists" : False},
            "scikey.status" : -2,
        }
    },
    {
        "$project" : {
            "email" : "$email",
            "id" : "$id"
        }
    },
    {
        "$limit" : 50000
    }
]

my_list = list(db.candidates.aggregate(pipeline))

client.close()
email_list = [li['email'] for li in my_list]
id_list = [li['id'] for li in my_list]
temp_arr = []
for x,y in zip(email_list,id_list):
    decrypt_data = [{
        "resources": {
            "email": x
        }
    }]
    result = requests.post(url=URL_decrypt_dev, data=json.dumps(decrypt_data),
                           headers={"Content-Type": "application/json"})
    temp_dict = {"email": result.json()['data'][0]['resources']['email'], "id" : y}
    print(temp_dict)
    temp_arr.append(temp_dict)
final_list = [dict(t) for t in {tuple(d.items()) for d in temp_arr}]
x = json.dumps(final_list)
with open('file.txt', 'w') as file:
    file.write(str(x))

df = pd.read_json('file.txt')
df.to_csv('data.csv', index=True)

# regex_pattern = re.compile('^\w+[\w-\.]*\@\w+((-\w+)|(\w*))\.[a-z]{2,3}$')
