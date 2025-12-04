import json

data_file = "data.json"

def load_data():
    with open(data_file, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)
        
def register_package():
    print("REGISTER PACKAGE")
    package_id = input("Package ID: ")
    sender_name = input("Sender Name: ")
    recipient = input("Recepient Name: ")
    phone = input("Recipient Phone: ")
    address = input("Recipient Address: ")
    weight = float(input("Package Weight(kg): "))
    category = input("Category (ex. fragile/perishable/large): ")
    
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
        "driver": None
    }
    
    data["packages"].append(new_package)    
    save_data(data)
    print("Package registered successfully!")
    
def view_packages():
    print(f"\nLIST OF PACKAGES\n{'-' * 100}")
    data = load_data()
    
    if not data["packages"]:
        print("No packages found.")
        return

    for package in data["packages"]:
        print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
        print(f"Address: {package['address']}, Phone: {package['phone']}")
        print(f"Weight: {package['weight']}kg, Category: {package['category']}")
        print(f"Status: {package['status']}, Route: {package['route_id']}, Driver: {package['driver']}\n{'-' * 100}")
        
def view_routes():
    print(f"LIST OF ROUTES\n{'-' * 100}")
    data = load_data()

    if not data["routes"]:
        print("No routes found.")
        return
    
    for route in data["routes"]:
        print(f"Route Name: {route['name']}, Driver: {route['driver']}")
        print(f"Packages: {', '.join(route['packages']) if route['packages'] else 'No packages assigned.'}\n{'-' * 100}")

def create_route():
    print("CREATE ROUTE")
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
    print("Route created successfully!\n")

def assign_package_to_route():
    print("Assign package to route")
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
    save_data(data)
    print("Package assigned to this route successfully!")
    
def assign_driver_to_route():
    print("ASSIGN DRIVER TO ROUTE")
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
            
    save_data(data)
    print("Driver assigned to route successfully!\n")
    
def dispatcher_menu(user):
    while True:
        print(f"\nDispatcher Menu ({user.username})")
        dis_menu = ["Register Package", "View All Packages", "Create Route", "View All Routes", "Assign Package to Route", "Assign Driver to Route", "Logout"]
        for i, d in zip(range(7), dis_menu):
            print(f"{i + 1}. {d}")
        
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                register_package()
            case 2:
                view_packages()
            case 3:
                create_route()
            case 4:
                view_routes()
            case 5:
                assign_package_to_route()
            case 6:
                assign_driver_to_route()
            case 7:
                print("Logging out...")
                break
            case _:
                print("Invalid Choice!\n")