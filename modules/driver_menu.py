import json

data_file = "data.json"

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)

# NEW: MorgsBranch save_data function
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def view_routes(user):
    print(f"\n\YOUR ASSIGNED ROUTES\n{'-' * 80}")
    data = load_data()
    
    if not data["routes"]:
        print("No routes found.")
        return
    
    for route, package in zip(data["routes"], data["packages"]):
        print(f"Route Name: {route['name']}, Driver: {route['driver']}, Status: {package['status']}\n{'-' * 80}")

# NEW: MorgsBranch view_assigned_packages function
def view_assigned_packages(driver_name):
    print(f"\nYOUR ASSIGNED PACKAGES\n{'-' * 80}")
    data = load_data()
    
    assigned_packages = [p for p in data["packages"] if p["driver"] == driver_name]
    
    if not assigned_packages:
        print("No packages assigned to you yet.")
        return
    
    for package in assigned_packages:
        print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
        print(f"Address: {package['address']}, Phone: {package['phone']}")
        print(f"Weight: {package['weight']}kg, Category: {package['category']}")
        print(f"Status: {package['status']}, Route: {package['route_id']}\n{'-' * 80}")

# NEW: MorgsBranch update_package_status function
def update_package_status(driver_name):
    data = load_data()
    package_id = input("Enter Package ID to update: ")
    
    package = None
    for p in data["packages"]:
        if p["package_id"] == package_id and p["driver"] == driver_name:
            package = p
            break
    
    if not package:
        print("Package not found or not assigned to you.")
        return
    
    print(f"\nCurrent Status: {package['status']}\n{'-' * 80}")
    print("1. Pending")
    print("2. In Transit")
    print(f"3. Delivered\n{'-' * 80}")
    status_choice = input(f"{'-' * 80}\nSelect new status: ")
    
    status_map = {"1": "Pending", "2": "In Transit", "3": "Delivered"}
    
    if status_choice not in status_map:
        print("Invalid choice.")
        return
    
    package["status"] = status_map[status_choice]
    save_data(data)
    print(f"Package {package_id} status updated to {package['status']}.")

def driver_menu(user):
    while True:
        print(f"\nDRIVER MENU ({user.username})\n{'-' * 80}")
        driver_menu_list = ["View Assigned Routes", "View Assigned Packages", "Update Package Status", "Logout"]
        for i, m in zip(range(4), driver_menu_list):
            print(f"{i + 1}, {m}")
        
        choice = input(f"{'-' * 80}\nEnter your choice: ")
        
        if choice == "1":
            view_routes(user)
        elif choice == "2":
            view_assigned_packages(user.username)
        elif choice == "3":
            update_package_status(user.username)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice!\n")