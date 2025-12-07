import json, csv
from fpdf import FPDF
# MorgsBranch admin_menu.py
data_report = "data.json"

def load_data():
    with open(data_report, "r") as report:
        return json.load(report)
    
def save_data(data):
    with open(data_report, "w") as report:
        json.dump(data, report, indent=4)

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
    print(f"\nREPORT\n{'-' * 80}")
    data = load_data()
    
    drivers = len([u["username"] for u in data["users"] if u["role"] == "driver"])
    routes = len([r["name"] for r in data["routes"]])
    total_packages = len(data["packages"])
    pending = len([p for p in data["packages"] if p["status"] == "Pending"])
    delivered = len([p for p in data["packages"] if p["status"] == "Delivered"])
    
    print(f"Drivers: {drivers}")
    print(f"Routes: {routes}")
    print(f"Total Packages: {total_packages}")
    print(f"Pending Packages: {pending}")
    print(f"Delivered Packages: {delivered}")

    with open("report.csv", "w", newline="") as report:
        writer = csv.writer(report)

        writer.writerow(["Driver", "Route", "Packages", "Status"])

        for driver in [u["username"] for u in data["users"] if u["role"] == "driver"]:
            driver_routes = [r for r in data["routes"] if r["driver"] == driver]

            if not driver_routes:
                writer.writerow([driver, "None", "None", "None"])
            else:
                for route in driver_routes:
                    package_ids = route["packages"]
                    statuses = []
                    for pid in package_ids:
                        pkg = next((p for p in data["packages"] if p["package_id"] == pid), None)
                        if pkg:
                            statuses.append(pkg["status"])

                    writer.writerow([
                        driver,
                        route["name"],
                        ", ".join(package_ids) if package_ids else "None",
                        ", ".join(statuses) if statuses else "None"
                    ])

    print("Detailed CSV report saved as report.csv")

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