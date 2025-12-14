import json
from user import load_data, save_data
from datetime import datetime, timedelta
        
def register_package():
    print("\nREGISTER PACKAGE")
    package_id = input("Package ID: ")
    sender_name = input("Sender Name: ")
    recipient = input("Recepient Name: ")
    phone = input("Recipient Phone: ")
    address = input("Recipient Address: ")
    weight = float(input("Package Weight(kg): "))
    category = input("Category (ex. fragile/perishable/large): ")
    expected_date = input("Expected Delivery Date (YYYY-MM-DD): ")
    
    data = load_data()
    
    for package in data["packages"]:
        if package["package_id"] == package_id:
            print("Package ID already exists.")
            return
    
    new_package = {
        "package_id": package_id,
        "sender_name": sender_name,
        "recipient": recipient,
        "phone": phone,
        "address": address,
        "weight": weight,
        "category": category,
        "status": "Pending",
        "route_id": None,
        "driver": None,
        "expected_date": expected_date,
        "date_registered": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "delivered_date": None
    }
    
    data["packages"].append(new_package)    
    save_data(data)
    print("Package registered successfully!")
    
def view_packages():
    print("\nLIST OF PACKAGES")
    data = load_data()
    
    if not data["packages"]:
        print("No packages found.")
        return

    for package in data["packages"]:
        print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
        print(f"Address: {package['address']}, Phone: {package['phone']}")
        print(f"Weight: {package['weight']}kg, Category: {package['category']}")
        print(f"Status: {package['status']}, Route: {package['route_id']}, Driver: {package['driver']}")
        

def create_route():
    print("\nCREATE ROUTE")
    route_name = input("Route Name: ")
    data = load_data()
    
    for route in data["routes"]:
        if route["name"] == route_name:
            print("Route already exists!")
            return
    
    new_route = {
        "name": route_name,
        "driver": None,
        "packages": []
    }
    
    data["routes"].append(new_route)
    save_data(data)
    print("Route created successfully!")

def assign_package_to_route():
    print("\nASSIGN PACKAGE TO ROUTE")
    data = load_data()
    
    package_id = input("Package ID: ")
    route_name = input("Route Name: ")
    
    package = None
    for packages in data["packages"]:
        if packages["package_id"] == package_id:
            package = packages
            break

    if package is None:
        print("Package not found!")
        return
    
    route = None
    for routes in data["routes"]:
        if routes["name"] == route_name:
            route = routes
            break
    
    if route is None:
        print("Route not found!")
        return
    
    if package_id in route["packages"]:
        print("Packaged already assigned to this route!")
        return
    
    route["packages"].append(package_id)
    package["route_id"] = route_name
    
    if route.get("driver"):
        package["driver"] = route["driver"]
        
    save_data(data)
    print("Package assigned to this route successfully!")
    
def assign_driver_to_route():
    print("\nASSIGN DRIVER TO ROUTE")
    data = load_data()
    route_name = input("Route Name: ")
    driver_name = input("Driver Name: ")
    
    driver = None
    for drivers in data["users"]:
        if drivers["username"] == driver_name and drivers["role"] == "driver":
            driver = drivers
            break

    if driver is None:
        print("Driver not found!")
        return
    
    route = None
    for routes in data["routes"]:
        if routes["name"] == route_name:
            route = routes
            break
    
    if route is None:
        print("Route not found!")
        return
    
    route["driver"] = driver_name
    
    for package_id in route["packages"]:
        package = None
        
        for packages in data["packages"]:
            if packages["package_id"] == package_id:
                package = packages
                break
        
        if package:
            package["driver"] = driver_name
            
    if route.get("driver"):
        package["driver"] = route["driver"]
            
    save_data(data)
    print("Driver assigned to route successfully!")
    
def view_delayed_packages():
    print("\nDELAYED PACKAGES")
    data = load_data()
    
    delayed_found = False
    today = datetime.now().date()
    
    for package in data["packages"]:
        expected = package.get("expected_date")
        delivery = package.get("delivery_date")
        
        if expected:
            expected_date = datetime.strptime(expected, "%Y-%m-%d").date()

            if today > expected_date and delivery is None:
                delayed_found = True
                print(f"ID: {package['package_id']} | Expected: {expected} | Status: {package['status']}")
                print(f"Recipient: {package['recipient']} | Address: {package['address']}\n")
                
    if not delayed_found:
        print("No delayed packages.\n")
    
def dispatcher_menu(user):
    while True:
        print(f"\nDispatcher Menu")
        print("1. Register Package")
        print("2. View All Packages")
        print("3. Create Route")
        print("4. Assign Package to Route")
        print("5. Assign Driver to Route")
        print("6. View Delayed Packages")
        print("7. Logout")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            register_package()
        elif choice == 2:
            view_packages()
        elif choice == 3:
            create_route()
        elif choice == 4:
            assign_package_to_route()
        elif choice == 5:
            assign_driver_to_route()
        elif choice == 6:
            view_delayed_packages()
        elif choice == 7:
            print("Logging out...\n")
            break
        else:
            print("Invalid Choice!\n")