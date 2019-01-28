from pymongo import MongoClient
import requests
import json

client = MongoClient("localhost", 27017)

URL_decrypt_dev = "http://10.0.5.4:8108/crypto/v1/decrypt?env=dev&orgname=hire&domain_name=scikey"
#URL_decrypt_qa = "http://10.0.4.4:8108/crypto/v1/decrypt?env=dev&orgname=hire&domain_name=scikey"

db = client.hire_scikey
collection = db.candidates

main_arr = []

location = ["Rajkot"]
skill_name = ["Ubuntu"]
for i in location:
    for j in skill_name:
        pipeline = [
            {"$match" : {"$and" :  [ {"professional_skills" : {"$exists" : True}} , {"preferred_job_locations" : {"$exists" : True}} ]}},
            {"$unwind" : "$preferred_job_locations"},
            {"$unwind" : "$professional_skills"},
            {"$match" : {"$and" : [ {"professional_skills.name" : j}, {"preferred_job_locations.city_name" : i} ]}},
            {"$project" : {"_id" : 0, "email" : "$email", "name" : "$name"}}
        ]

        #[
        #    {"$match" : {"$and" :  [ {"professional_skills" : {"$exists" : True}} , {"preferred_job_locations" : {"$exists" : True}} ]}},
        #    {"$unwind" : "$preferred_job_locations"},
        #    {"$unwind" : "$professional_skills"},
        #    {"$match" : {"$and" : [ {"professional_skills.name" : j}, {"preferred_job_locations.city_name" : i} ]}},
        #    {"$project" : {"_id" : 0, "email" : "$email", "contact" : "$contact", "skill_name" : "$professional_skills.name", "city_name" : "$preferred_job_locations.city_name"}}
        #]

        my_list = list(db.candidates.aggregate(pipeline))

        email_list = [li['email'] for li in my_list]
        name_list = [li['name'] for li in my_list]

        print("Data for skill_name  " + j + " and for location " + i + "  Fetching ..." )
        # a = 0
        temp_arr = []
        for z,y in zip(email_list,name_list):
            decrypt_data = [{
                "resources": {
                    "email": z
                }
            }]
            result = requests.post(url=URL_decrypt_dev, data=json.dumps(decrypt_data),
                                       headers={"Content-Type": "application/json"})
            temp_dict = {"email" : result.json()['data'][0]['resources']['email'], "name" : y,"location" : i,"skill" : j}
            temp_arr.append(temp_dict)
        final_list = [dict(t) for t in {tuple(d.items()) for d in temp_arr}]
        print(final_list)
        print("\n")
    print("\n")