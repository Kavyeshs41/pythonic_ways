import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('skills_taxonomy').sheet1

data = sheet.get_all_records()

for onedata in data:
    onedata.pop('', None)
    onedata["skill_name"] = onedata["Skill Name"]
    onedata["synonyms"] = onedata["Synonyms (comma separated)"]
    del onedata["Synonyms (comma separated)"], onedata["Skill Name"]
    if onedata["synonyms"] == "":
        del onedata["synonyms"], onedata["skill_name"]

print(data)
print(data)



