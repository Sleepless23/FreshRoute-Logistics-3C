import json

data_file = "data.json"

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def view_assigned_packages(driver_name):
    print("\n=== YOUR ASSIGNED PACKAGES ===")
    data = load_data()
    
    assigned_packages = [p for p in data["packages"] if p["driver"] == driver_name]
    
    if not assigned_packages:
        print("No packages assigned to you yet.")
        return
    
    for package in assigned_packages:
        print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
        print(f"Address: {package['address']}, Phone: {package['phone']}")
        print(f"Weight: {package['weight']}kg, Category: {package['category']}")
        print(f"Status: {package['status']}, Route: {package['route_id']}")
        print("-" * 40)

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
    
    print(f"Current Status: {package['status']}")
    print("1. Pending")
    print("2. In Transit")
    print("3. Delivered")
    status_choice = input("Select new status: ")
    
    status_map = {"1": "Pending", "2": "In Transit", "3": "Delivered"}
    
    if status_choice not in status_map:
        print("Invalid choice.")
        return
    
    package["status"] = status_map[status_choice]
    save_data(data)
    print(f"Package {package_id} status updated to {package['status']}.")

def driver_menu(user):
    while True:
        print(f"\n=== DRIVER MENU ({user.username}) ===")
        print("1. View Assigned Packages")
        print("2. Update Package Status")
        print("3. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_assigned_packages(user.username)
        elif choice == "2":
            update_package_status(user.username)
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice!\n")