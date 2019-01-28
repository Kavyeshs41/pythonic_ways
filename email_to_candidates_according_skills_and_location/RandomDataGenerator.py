import json

import requests
import random
import csv

a = requests.get("http://uinames.com/api/?region=india&amount=100")

b = a.json()
primary_skills = ["Java EE","AWS","Node.js","Python","ASP.NET","PHP","Java","Android","Angular","C++","Java","JavaScript","PHP","ASP.NET","HTML, CSS","Angular","Node.js","Ruby","ApacheSpark","Hadoop","Java",".NET","Docker","Java","Angular","Node.js","Javascript","HTML","CSS","JMeter","Node.js","Angular","Core Java","Java","Java",".NET","Python","Scala","Ruby","MongoDB","Java","Angular","Python",".NET","Andriod","Machine Learning","Docker","Hadoop","JavaScript","Agile"]
other_skills = ["PostgreSQL","Amazon API","MongoDB","MATLAB","MySQL Server","MySQL","MySQL","SQLite","MongoDB","C","PostgreSQL","Team Management","Product Management","MongoDB","Good Communication","Team Management","Product Management","Management","PostgreSQL","MongoDB","ScrumMaster","Project Management","Product Delivery Management","Communication","Time management","Decision Making","Self-motivation","Leadership","Conflict Resolution","Adaptability","Communication skills","Project Management","Product Delivery Management","Communication skills","Project Management","ScrumMaster","ScrumMaster","Business Analyst","ScrumMaster","Project Management","NodeJS","Node JS","Project Management","Time Management","Jmeter","LeaderShip","Communication","Presentation Skill","HTML","Computer Graphics"]
location = ["India -> Surat","India -> Pune, Mumbai","India -> Pune","India -> Pune, Mumbai, Surat","India -> Surat, Mumbai","India -> Pune, Bengaluru, Surat","India -> Surat, Mumbai, Bengaluru","India -> Pune, Bengaluru","India -> Surat, Mumbai","India -> Pune, Mumbai, Surat","India -> Pune, Bengaluru","India -> Pune, Mumbai","India -> Surat, Bangaluru","India -> Surat","India -> Pune, Mumbai","India -> Mumbai","India -> Surat, Bangaluru, Pune","India -> Mumbai","India -> Surat","India ->Mumbai,Bangaluru","India ->Bangaluru"]
some_email_domains = ["rupaymail.com","1thecity.biz","mailmy.com","bitmail.com","rupaymail.com","youmail.com"]
new_json = []
for _, value in enumerate(b, 1):
    sr_no = int(_)
    name = str(value["name"] + " " + value["surname"])
    email = str(value["name"] + "." + value["surname"] + "@" + some_email_domains[random.randint(0, len(some_email_domains)-1)]).lower()
    password = 12345678
    mob = random.randint(1800000000, 5999999999)
    p_skill = primary_skills[random.randint(0, len(primary_skills)-1)]
    o_skill = other_skills[random.randint(0, len(other_skills)-1)]
    p_location = location[random.randint(0, len(location)-1)]
    exp = random.randint(1, 120)
    resume_file = ""
    resume_contents = str(value["name"] + " " + value["surname"])
    if value["gender"] == "male":
        img = str("https://randomuser.me/api/portraits/men/" + str(random.randint(1, 99)) + ".jpg")
    else:
        img = str("https://randomuser.me/api/portraits/women/" + str(random.randint(1, 99)) + ".jpg")
    data = {
        "Sr. No" : sr_no,
        "First & Last Name" : name,
        "Email" : email,
        "Password" : password,
        "Mobile" : mob,
        "Primary Skills" : p_skill,
        "Other Skills" : o_skill,
        "Exp in months" : exp,
        "Job Locations" : p_location,
        "Resume File" : resume_file,
        "Resume Contents" : resume_contents,
        "Profile Image" : img
    }
    new_json.append(data)

f=csv.writer(open("data.csv","w", newline=''))
f.writerow(["Sr. No", "First & Last Name", "Email", "Password", "Mobile", "Primary Skills","Other Skills","Exp in months","Job Locations","Resume File","Resume Contents","Profile Image"])

for i in new_json:
    f.writerow([i["Sr. No"],i["First & Last Name"], i["Email"], i["Password"], i["Mobile"], i["Primary Skills"],i["Other Skills"],i["Exp in months"],i["Job Locations"],
               i["Resume File"],i["Resume Contents"],i["Profile Image"]])