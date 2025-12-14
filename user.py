import json

data_file = "data.json"

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)
        
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        
def auth(username, password):
    data = load_data()
    
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return User(username=user["username"], role=user["role"])
        
    return None

def add_user(username, password, role):
    data = load_data()
    
    for user in data["users"]:
        if user["username"] == username:
            return False
        
    data["users"].append({
        "username": username,
        "password": password,
        "role": role
    })    
    
    save_data(data)
    return True