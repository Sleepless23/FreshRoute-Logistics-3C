import json

data_file = "data.json"

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)

def view_routes(user):
    print(f"\nYOUR ASSIGNED ROUTES\n{'-' * 100}")
    data = load_data()
    
    if not data["routes"]:
        print("No routes found.")
        return
    
    for route, package in zip(data["routes"], data["packages"]):
        print(f"Route Name: {route['name']}, Driver: {route['driver']}, Status: {package['status']}\n{'-' * 100}")

def driver_menu(user):
    print(f"\n=== DRIVER MENU ({user.username}) ===")
    dri_menu = ["View Assigned Routes", "Logout"]

    for i, d in zip(range(2), dri_menu):
        print(f"{i + 1}. {d}")

    driver_input = input("Enter your choice: ")

    match driver_input:
        case "1":
            view_routes(user)
        case "2":
            print("Logging out...")