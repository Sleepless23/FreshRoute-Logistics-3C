import json
import os
# MorgsBranch admin_menu.py
data_file = "data.json"

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def view_all_packages():
    print(f"\nALL PACKAGES\n{'-' * 80}")
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
    print(f"\nALL ROUTES\n{'-' * 80}")
    data = load_data()
    
    if not data["routes"]:
        print("No routes found.")
        return
    
    for route in data["routes"]:
        print(f"Route Name: {route['name']}, Driver: {route['driver']}")
        print(f"Packages: {', '.join(route['packages']) if route['packages'] else 'None'}\n{'-' * 80}")

def view_all_users():
    print(f"\nALL USERS\n{'-' * 80}")
    data = load_data()
    
    dispatchers = [u["username"] for u in data["users"] if u["role"] == "dispatcher"]
    drivers = [u["username"] for u in data["users"] if u["role"] == "driver"]
    
    print(f"Dispatchers: {', '.join(dispatchers) if dispatchers else 'None'}")
    print(f"Drivers: {', '.join(drivers) if drivers else 'None'}\n{'-' * 80}")

def generate_report():
    print("\nREPORT\n{'-' * 80}")
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

    print("Create file report:\n1. CSV\n2. PDF")
    file_report = input("\n Select File Format: ")
    
    match file_report:
        case "1":
            head1 = "DRIVER"
            head2 = "PACKAGE_OWNER"
            head3 = "ASSIGNMENT"
            _header = [f"{head1:^10}{head2:^20}{head3:^10}  "]
            os.system(f"echo {_header} > report.csv")

            driver_report = [ur["username"] for ur in data["users"] if ur["role"] == "driver"]
            for driver in drivers:
                count_report = len([pr for pr in data["packages"] if pr["driver"] == driver])
                os.system(f"echo {driver_report}, {count_report} >> report.csv")
        case _:
            print("null")

def admin_menu(user):
    while True:
        print(f"\nADMIN MENU ({user.username})\n{'-' * 80}")
        admin_menu_list = ["View All Packages", "View All Routes", "View Drivers / Dispatchers", "Generate Report", "Logout"]
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