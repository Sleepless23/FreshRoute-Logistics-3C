import json
# MorgsBranch admin_menu.py
data_file = "data.json"

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def view_all_packages():
    print(f"\n\033[45mALL PACKAGES\033[0m\n{'-' * 80}")
    data = load_data()
    
    if not data["packages"]:
        print("No packages found.")
        return
    
    for package in data["packages"]:
        print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
        print(f"Address: {package['address']}, Phone: {package['phone']}")
        print(f"Weight: {package['weight']}kg, Category: {package['category']}")
        print(f"Status: {package['status']}, Route: {package['route_id']}, Driver: {package['driver']}\n{'-' * 80}")

def view_all_routes():
    print(f"\n\033[42mALL ROUTES\033[0m\n{'-' * 80}")
    data = load_data()
    
    if not data["routes"]:
        print("No routes found.")
        return
    
    for route in data["routes"]:
        print(f"Route Name: {route['name']}, Driver: {route['driver']}")
        print(f"Packages: {', '.join(route['packages']) if route['packages'] else 'None'}\n{'-' * 80}")

def view_all_users():
    print(f"\n\033[43mALL USERS\033[0m\n{'-' * 80}")
    data = load_data()
    
    dispatchers = [u["username"] for u in data["users"] if u["role"] == "dispatcher"]
    drivers = [u["username"] for u in data["users"] if u["role"] == "driver"]
    
    print(f"Dispatchers: {', '.join(dispatchers) if dispatchers else 'None'}")
    print(f"Drivers: {', '.join(drivers) if drivers else 'None'}\n{'-' * 80}")

def generate_report():
    print("\n\033[46mREPORT\033[0m\n{'-' * 80}")
    data = load_data()
    
    total_packages = len(data["packages"])
    pending = len([p for p in data["packages"] if p["status"] == "Pending"])
    delivered = len([p for p in data["packages"] if p["status"] == "Delivered"])
    
    print(f"Total Packages: {total_packages}")
    print(f"Pending Packages: {pending}")
    print(f"Delivered Packages: {delivered}")

    drivers = [u["username"] for u in data["users"] if u["role"] == "driver"]
    for driver in drivers:
        count = len([p for p in data["packages"] if p["driver"] == driver])
        print(f"{driver}: {count} packages assigned")

def admin_menu(user):
    while True:
        print(f"\n\033[41mADMIN MENU ({user.username})\033[0m\n{'-' * 80}")
        admin_menu_list = ["\033[95mView All Packages\033[0m", "\033[92mView All Routes\033[0m", "\033[93mView Drivers / Dispatchers\033[0m", "\033[94mGenerate Report\033[0m", "\033[91mLogout\033[0m"]
        for i, m in zip(range(5), admin_menu_list):
            print(f"{i + 1}. {m}")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_all_packages()
        elif choice == "2":
            view_all_routes()
        elif choice == "3":
            view_all_users()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice!\n")