# [Sean's Branch](#SeanBranch)
---
## [Update Log:](#Updates)
## [12/6/2025 Added MorgsBranch functions to admin_menu.py and driver_menu.py](#Update1.1}
## [12/5/2025 Pushed Charles' files from Selrach Branch](#Update1.0)
## [Changes:](#Changes)
---
***12/6/2025***
---
- **Added** functions from **<mark>MorgsBranch</mark>** to <mark>*admin_menu.py*</mark> and <mark>*driver_menu.py*</mark>
- **Customized String Colorization** for **readability**, easier to distinguish menu options for all .py files
---
### MorgsBranch (Save Data)
> ```
> def save_data(data):
>    with open(data_file, "w") as file:
>        json.dump(data, file, indent=4)
> ```
### MorgsBranch (View Assigned Packages)
> ```
> def view_assigned_packages(driver_name):
>    print("\n=== YOUR ASSIGNED PACKAGES ===")
>    data = load_data()
>    
>    assigned_packages = [p for p in data["packages"] if p["driver"] == driver_name]
>    
>    if not assigned_packages:
>        print("No packages assigned to you yet.")
>        return
>    
>    for package in assigned_packages:
>        print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
>        print(f"Address: {package['address']}, Phone: {package['phone']}")
>        print(f"Weight: {package['weight']}kg, Category: {package['category']}")
>        print(f"Status: {package['status']}, Route: {package['route_id']}")
>        print("-" * 40)
> ```
### MorgsBranch (Update Package)
> ```
> def update_package_status(driver_name):
>    data = load_data()
>    package_id = input("Enter Package ID to update: ")
>    
>    package = None
>    for p in data["packages"]:
>        if p["package_id"] == package_id and p["driver"] == driver_name:
>            package = p
>            break
>    
>    if not package:
>        print("Package not found or not assigned to you.")
>        return
>    
>    print(f"Current Status: {package['status']}")
>    print("1. Pending")
>    print("2. In Transit")
>    print("3. Delivered")
>    status_choice = input("Select new status: ")
>    
>    status_map = {"1": "Pending", "2": "In Transit", "3": "Delivered"}
>    
>    if status_choice not in status_map:
>        print("Invalid choice.")
>        return
>    
>    package["status"] = status_map[status_choice]
>    save_data(data)
>    print(f"Package {package_id} status updated to {package['status']}.")
> ```
---
***12/5/2025***
---
- **Adjusted** print command in main.py
- **Adjusted** method *view_packages()* and **improved** print readability for every menu for <mark>main.py</mark> and <mark>dispatcher_menu.py</mark>
- **Added** method *view_routes()* in <mark>dispatcher_menu.py</mark>
- **Converted** nested if statement into Switch/Match case for method <mark>dispatcher_menu</mark>
- **Added** *import json*, added variable *data_file*, added new methods *load_data()*, *view_routes()* to <mark>driver_menu.py</mark>
---
## [main.py](#main)
### From:
> ```
> def main():
>     while True:
>         print("FreshRoute Logistics System")
>         print("1. Login")
>         print("2. Register")
>         print("3. Exit")
>         
>         choice = int(input("Enter your choice: "))
>         
>         if choice == 1:
>             user = login()
>             if not user:
>                 continue
>             
>             if user.role == "admin":
>                 admin_menu(user)
>             elif user.role == "dispatcher":
>                 dispatcher_menu(user)
>             elif user.role == "driver":
>                 driver_menu(user)
>                 
>         elif choice == 2:
>             register()
>             
>         elif choice == 3:
>             print("Bye-bye!")
>             break
>         
>         else:
>             print("Invalid choice.\n")
>  ```
### To:
> ```
> def main():
>     while True:
>         print("FreshRoute Logistics System")
>         login_menu = ['Login', 'Register', 'Exit']
>         for i, m in zip(range(4), login_menu):
>             print(f"{i + 1}. {m}")
>         
>         choice = int(input("Enter your choice: "))
>         
>         match choice:
>             case 1:
>                 user = login()
>                 if not user:
>                     continue
>                 match user.role:
>                     case "admin":
>                         admin_menu(user)
>                     case "dispatcher":
>                         dispatcher_menu(user)
>                     case "driver":
>                         driver_menu(user)        
>             case 2:
>                 register()
>             case 3:
>                 print("Bye-bye!")
>                 break
>             case _:
>                 print("Invalid choice.\n")
>  ```
---
## [dispatcher_menu.py](#dispatcher_menu)
### From:
>```
> def register_package():
>     print("REGISTER PACKAGE")
>     package_id = input("Package ID: ")
>     sender_name = input("Sender Name: ")
>     recipient = input("Recepient Name: ")
>     phone = input("Recipient Phone: ")
>     address = input("Recipient Address: ")
>     weight = float(input("Package Weight(kg): "))
>     category = input("Category (ex. fragile/perishable/large): ")
>     
>     data = load_data()
>     
>     for package in data["packages"]:
>         if package["package_id"] == package_id:
>             print("Package ID already exists.")
>             return
>     
>     new_package = {
>         "package_id": package_id,
>         "sender_name": sender_name,
>         "recipient": recipient,
>         "phone": phone,
>         "address": address,
>         "weight": weight,
>         "category": category,
>         "status": "Pending",
>         "route_id": None,
>         "driver": None
>     }
>     
>     data["packages"].append(new_package)    
>     save_data(data)
>     print("Package registered successfully!")
>     
> def view_packages():
>     print("LIST OF PACKAGES")
>     data = load_data()
>     
>     if not data["packages"]:
>         print("No packages found.")
>         return
> 
>     for package in data["packages"]:
>         print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
>         print(f"Address: {package['address']}, Phone: {package['phone']}")
>         print(f"Weight: {package['weight']}kg, Category: {package['category']}")
>         print(f"Status: {package['status']}, Route: {package['route_id']}, Driver: {package['driver']}")
>         
> 
> def create_route():
>     print("CREATE ROUTE")
>     route_name = input("Route Name: ")
>     data = load_data()
>     
>     for route in data["routes"]:
>         if route["name"] == route_name:
>             print("Route already exists!")
>             return
>     
>     new_route = {
>         "name": route_name,
>         "driver": None,
>         "packages": []
>     }
>     
>     data["routes"].append(new_route)
>     save_data(data)
>     print("Route created successfully!\n")
> 
> def assign_package_to_route():
>     print("Assign package to route")
>     data = load_data()
>     
>     package_id = input("Package ID: ")
>     route_name = input("Route Name: ")
>     
>     package = None
>     for packages in data["packages"]:
>         if packages["package_id"] == package_id:
>             package = packages
>             break
> 
>     if package is None:
>         print("Package not found!")
>         return
>     
>     route = None
>     for routes in data["routes"]:
>         if routes["name"] == route_name:
>             route = routes
>             break
>     
>     if route is None:
>         print("Route not found!")
>         return
>     
>     if package_id in route["packages"]:
>         print("Packaged already assigned to this route!")
>         return
>     
>     route["packages"].append(package_id)
>     package["route_id"] = route_name
>     save_data(data)
>     print("Package assigned to this route successfully!")
>     
> def assign_driver_to_route():
>     print("ASSIGN DRIVER TO ROUTE")
>     data = load_data()
>     route_name = input("Route Name: ")
>     driver_name = input("Driver Name: ")
>     
>     driver = None
>     for drivers in data["users"]:
>         if drivers["username"] == driver_name and drivers["role"] == "driver":
>             driver = drivers
>             break
> 
>     if driver is None:
>         print("Driver not found!")
>         return
>     
>     route = None
>     for routes in data["routes"]:
>         if routes["name"] == route_name:
>             route = routes
>             break
>     
>     if route is None:
>         print("Route not found!")
>         return
>     
>     route["driver"] = driver_name
>     
>     for package_id in route["packages"]:
>         package = None
>         
>         for packages in data["packages"]:
>             if packages["package_id"] == package_id:
>                 package = packages
>                 break
>         
>         if package:
>             package["driver"] = driver_name
>             
>     save_data(data)
>     print("Driver assigned to route successfully!\n")
>     
> def dispatcher_menu(user):
>     while True:
>         print(f"\nDispatcher Menu ({user.username})")
>         print("1. Register Package")
>         print("2. View All Packages")
>         print("3. Create Route")
>         print("4. Assign Package to Route")
>         print("5. Assign Driver to Route")
>         print("6. Logout")
>         
>         choice = int(input("Enter your choice: "))
>         
>         if choice == 1:
>             register_package()
>         elif choice == 2:
>             view_packages()
>         elif choice == 3:
>             create_route()
>         elif choice == 4:
>             assign_package_to_route()
>         elif choice == 5:
>             assign_driver_to_route()
>         elif choice == 6:
>             print("Logging out...")
>             break
>         else:
>             print("Invalid Choice!\n")
> ```
### To:
> ```
> def register_package():
>     print(f"\nREGISTER PACKAGE{'-' * 100}")
>     package_id = input("Package ID: ")
>     sender_name = input("Sender Name: ")
>     recipient = input("Recepient Name: ")
>     phone = input("Recipient Phone: ")
>     address = input("Recipient Address: ")
>     weight = float(input("Package Weight(kg): "))
>     category = input("Category (ex. fragile/perishable/large): ")
>     
>     data = load_data()
>     
>     for package in data["packages"]:
>         if package["package_id"] == package_id:
>             print("Package ID already exists.")
>             return
>     
>     new_package = {
>         "package_id": package_id,
>         "sender_name": sender_name,
>         "recipient": recipient,
>         "phone": phone,
>         "address": address,
>         "weight": weight,
>         "category": category,
>         "status": "Pending",
>         "route_id": None,
>         "driver": None
>     }
>     
>     data["packages"].append(new_package)    
>     save_data(data)
>     print("Package registered successfully!")
>     
> def view_packages():
>     print(f"\nLIST OF PACKAGES\n{'-' * 100}")
>     data = load_data()
>     
>     if not data["packages"]:
>         print("No packages found.")
>         return
> 
>     for package in data["packages"]:
>         print(f"ID: {package['package_id']}, Sender: {package['sender_name']}, Recipient: {package['recipient']}")
>         print(f"Address: {package['address']}, Phone: {package['phone']}")
>         print(f"Weight: {package['weight']}kg, Category: {package['category']}")
>         print(f"Status: {package['status']}, Route: {package['route_id']}, Driver: {package['driver']}\n{'-' * 100}")
>         
> def view_routes():
>     print(f"\nLIST OF ROUTES\n{'-' * 100}")
>     data = load_data()
> 
>     if not data["routes"]:
>         print("No routes found.")
>         return
>     
>     for route in data["routes"]:
>         print(f"Route Name: {route['name']}, Driver: {route['driver']}")
>         print(f"Packages: {', '.join(route['packages']) if route['packages'] else 'No packages assigned.'}\n{'-' * 100}")
> 
> def create_route():
>     print(f"\nCREATE ROUTE\n{'-' * 100}")
>     route_name = input("Route Name: ")
>     data = load_data()
>     
>     for route in data["routes"]:
>         if route["name"] == route_name:
>             print("Route already exists!")
>             return
>     
>     new_route = {
>         "name": route_name,
>         "driver": None,
>         "packages": []
>     }
>     
>     data["routes"].append(new_route)
>     save_data(data)
>     print("Route created successfully!\n")
> 
> def assign_package_to_route():
>     print(f"\nAssign package to route\n{'-' * 100}")
>     data = load_data()
>     
>     package_id = input("Package ID: ")
>     route_name = input("Route Name: ")
>     
>     package = None
>     for packages in data["packages"]:
>         if packages["package_id"] == package_id:
>             package = packages
>             break
> 
>     if package is None:
>         print("Package not found!")
>         return
>     
>     route = None
>     for routes in data["routes"]:
>         if routes["name"] == route_name:
>             route = routes
>             break
>     
>     if route is None:
>         print("Route not found!")
>         return
>     
>     if package_id in route["packages"]:
>         print("Packaged already assigned to this route!")
>         return
>     
>     route["packages"].append(package_id)
>     package["route_id"] = route_name
>     save_data(data)
>     print("Package assigned to this route successfully!")
>     
> def assign_driver_to_route():
>     print(f"\nASSIGN DRIVER TO ROUTE\n{'-' * 100}")
>     data = load_data()
>     route_name = input("Route Name: ")
>     driver_name = input("Driver Name: ")
>     
>     driver = None
>     for drivers in data["users"]:
>         if drivers["username"] == driver_name and drivers["role"] == "driver":
>             driver = drivers
>             break
> 
>     if driver is None:
>         print("Driver not found!")
>         return
>     
>     route = None
>     for routes in data["routes"]:
>         if routes["name"] == route_name:
>             route = routes
>             break
>     
>     if route is None:
>         print("Route not found!")
>         return
>     
>     route["driver"] = driver_name
>     
>     for package_id in route["packages"]:
>         package = None
>         
>         for packages in data["packages"]:
>             if packages["package_id"] == package_id:
>                 package = packages
>                 break
>         
>         if package:
>             package["driver"] = driver_name
>             
>     save_data(data)
>     print("Driver assigned to route successfully!\n")
>     
> def dispatcher_menu(user):
>     while True:
>         print(f"\nDispatcher Menu ({user.username})\n{'-' * 100}")
>         dis_menu = ["Register Package", "View All Packages", "Create Route", "View All Routes", "Assign Package to Route", "Assign Driver to Route", "Logout"]
>         for i, d in zip(range(7), dis_menu):
>             print(f"{i + 1}. {d}")
>         
>         choice = int(input("Enter your choice: "))
> 
>         match choice:
>             case 1:
>                 register_package()
>             case 2:
>                 view_packages()
>             case 3:
>                 create_route()
>             case 4:
>                 view_routes()
>             case 5:
>                 assign_package_to_route()
>             case 6:
>                 assign_driver_to_route()
>             case 7:
>                 print("Logging out...")
>                 break
>             case _:
>                 print("Invalid Choice!\n")
> ```
---
## [driver_menu.py](#driver_menu)
### From:
> ```
> def driver_menu(user):
>     print(f"\n=== DRIVER MENU ({user.username}) ===")
>     input("Press Enter to logout...")
> ```
### To:
> ```
> import json
> 
> data_file = "data.json"
> 
> def load_data():
>     with open(data_file, "r") as file:
>         return json.load(file)
> 
> def view_routes(user):
>     print(f"\nYOUR ASSIGNED ROUTES\n{'-' * 100}")
>     data = load_data()
>     
>     if not data["routes"]:
>         print("No routes found.")
>         return
>     
>     for route, package in zip(data["routes"], data["packages"]):
>         print(f"Route Name: {route['name']}, Driver: {route['driver']}, Status: {package['status']}\n{'-' * 100}")
> 
> def driver_menu(user):
>     print(f"\n=== DRIVER MENU ({user.username}) ===")
>     dri_menu = ["View Assigned Routes", "Logout"]
> 
>     for i, d in zip(range(2), dri_menu):
>         print(f"{i + 1}. {d}")
> 
>     driver_input = input("Enter your choice: ")
> 
>     match driver_input:
>         case "1":
>             view_routes(user)
>         case "2":
>             print("Logging out...")
> ```
