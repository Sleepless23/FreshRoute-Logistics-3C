import json
from user import load_data, save_data
from datetime import datetime

def view_assign_packages(username):
    print("\nYOUR ASSIGNED PACKAGES")
    data = load_data()
    
    found = False
    
    for package in data["packages"]:
        if package["driver"] == username:
            found = True
            print(f"Package ID: {package['package_id']}")
            print(f"Recipient: {package['recipient']}")
            print(f"Address: {package['address']}")
            print(f"Status: {package['status']}")
            print(f"Route: {package['route_id']}")
            
    if not found:
        print("No assigned packages.")
        
def update_package_status(username):
    print("\nUPDATE PACKAGE STATUS")
    data = load_data()
    
    package_id = input("Enter Package ID: ")
    for packages in data["packages"]:
        if packages["package_id"] == package_id and packages["driver"] == username:
            package = packages
            break
        
    if package is None:
        print("Package not found or not assigned to you.")
        return
    
    print("\nSelect new status:")
    print("1. Out for Delivery")
    print("2. Delivered")
    
    choice = int(input("New Status: "))
    
    if choice == 1:
        package["status"] = "Out for Delivery"
        
    elif choice == 2:
        package["status"] = "Delivered"
        note = input("Enter delivery note: ")
        package["delivery_note"] = note
        package["actual_delivery_date"] = datetime.now().strftime("%Y-%m-%d")

    else:
        print("Invalid option.")
        return
    
    save_data(data)
    print("Status updated successfully.")
    
def view_route(username):
    print("\nYOUR ROUTE")
    data = load_data()
    
    route_found = None
    
    for route in data['routes']:
        if route['driver'] == username:
            route_found = route
            break
    
    if route_found is None:
        print("No route assigned.")
        return
    
    print(f"\nRoute name: {route_found['name']}")
    print("Packages:")
    
    for package_id in route_found['packages']:
        print(f"- {package_id}")
        
    print()
    
def driver_menu(user):
    while True:
        print(f"\nDriver Menu")
        print("1. View Assigned Packages")
        print("2. Update Package Status")
        print("3. View Route")
        print("4. Logout")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            view_assign_packages(user.username)
        elif choice == 2:
            update_package_status(user.username)
        elif choice == 3:
            view_route(user.username)
        elif choice == 4:
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")
        