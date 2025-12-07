import json, csv

data_file = 'data.json'

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)
    
data = load_data()

users = data["users"]
if users == "username":
    username = users

print(username)