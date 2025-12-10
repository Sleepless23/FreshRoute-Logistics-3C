import json, csv
from user import load_data, save_data, add_user
from datetime import datetime
from fpdf import FPDF

def view_users():
    data = load_data()
    
    print("\nLIST OF USERS")
    if not data["users"]:
        print("No registered users yet.")
        return
    
    for users in data["users"]:
        print(f"Username: {users['username']} | Role: {users['role']}")
    print()
    
def delete_user():
    data = load_data()
    
    print("\nDELETE USER")
    username = input("Enter username to delete: ")
    confirmation = input("Do you really want to delete (Y/N)?: ").lower()
    
    if confirmation == 'y':
        for user in data["users"]:
            if user["username"] == username:
                data["users"].remove(user)
                save_data(data)
                print(f"User '{username}' deleted successfully.\n")
                return
            
        print("User not found.")
            
    elif confirmation == 'n':
        print("Cancelled delete.")
        return
    
    else:
        print("Enter correct input only.")
        
def create_user():
    print("\nADD NEW USER")
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm = input("Confirm password: ")
    
    if password != confirm:
        print("Passwords do not match.\n")
        return
    
    print("Select role:")
    print("1. Admin")
    print("2. Dispatcher")
    print("3. Driver")
    
    role_input = int(input("Role: "))
    
    roles = {
        1: "admin",
        2: "dispatcher",
        3: "driver"
    }
    
    if role_input not in roles:
        print("Invalid role.\n")
        return
    
    role = roles[role_input]
    
    if add_user(username, password, role):
        print("User created successfully!")
    else:
        print("Username already taken.")
        
def view_system_data():
    data = load_data()
    
    print("\nSYSTEM DATA")
    print(f"Total users: {len(data['users'])}")
    print(f"Total packages: {len(data['packages'])}")
    print(f"Total routes: {len(data['routes'])}")
    
    print()
    
def view_package_status():
    data = load_data()
    
    if not data['packages']:
        print("\nNo packages found.\n")
        return
    
    pending = []
    out_for_delivery = []
    delivered = []
    delayed = []
    
    today = datetime.now().date()
    
    for package in data['packages']:
        expected_str = package.get("expected_delivery") or package.get("expected_date")
        delivered_str = package.get("delivered_date") or package.get("delivered_date")
        
        expected_date = None
        
        if expected_str:
            try:
                expected_date = datetime.strptime(expected_str, "%Y-%m-%d").date()
            except:
                pass
        
        delivered_date = None
        
        if delivered_str:
            try:
                delivered_date = datetime.strptime(delivered_str[:10], "%Y-%m-%d").date()
            except:
                pass
        
        if package['status'] != "Delivered" and expected_date and today > expected_date:
            delayed.append(package)
        elif package['status'] == "Pending":
            pending.append(package)
        elif package['status'] == "Out for Delivery":
            out_for_delivery.append(package)
        elif package['status'] == "Delivered":
            delivered.append(package)

    def print_packages(package_list, title):
        if package_list:
            print(f"{title}")
            for package in package_list:
                print(f"ID: {package['package_id']}, Recipient: {package['recipient']}, Driver: {package['driver']}, Status: {package['status']}, Expected: {expected_str or '-'}, Delivered: {delivered_str or '-'}")
    
    print_packages(pending, "Pending Packages")
    print_packages(out_for_delivery, "Out for Delivery")
    print_packages(delivered, "Delivered Packages")
    print_packages(delayed, "Delayed Packages")

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
        
def export_packages_csv():
    data = load_data()
    
    if not data["packages"]:
        print("No packages to export.\n")
        return
    
    filename = input("Enter CSV filename (example: report.csv): ")
    
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Package ID", "Sender", "Recipient", "Address", "Phone", "Weight", "Category", "Status", "Route", "Driver", "Expected Date", "Delivered Date", "Delivery Note"])
        
        for package in data["packages"]:
            writer.writerow([
                package.get("package_id","-"),
                package.get("sender_name","-"),
                package.get("recipient","-"),
                package.get("address","-"),
                package.get("phone","-"),
                package.get("weight","-"),
                package.get("category","-"),
                package.get("status","-"),
                package.get("route_id","-"),
                package.get("driver","-"),
                package.get("expected_date","-"),
                package.get("delivered_date","-"),
                package.get("delivery_note","-")
            ])
    print(f"Packages exported successfully to {filename}!\n")
    
def export_packages_pdf():
    data = load_data()
    
    if not data["packages"]:
        print("No packages to export.\n")
        return
    
    filename = input("Enter PDF filename (example: report.pdf): ")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    
    pdf.cell(0, 10, "Package Report", ln=True, align="C")
    pdf.ln(5)
    
    pdf.set_font("Arial", "", 10)
    
    for package in data["packages"]:
        pdf.cell(0, 6, f"ID: {package.get('package_id','-')}, Sender: {package.get('sender_name','-')}, Recipient: {package.get('recipient','-')}", ln=True)
        pdf.cell(0, 6, f"Address: {package.get('address','-')}, Phone: {package.get('phone','-')}, Weight: {package.get('weight','-')}kg, Category: {package.get('category','-')}", ln=True)
        pdf.cell(0, 6, f"Status: {package.get('status','-')}, Route: {package.get('route_id','-')}, Driver: {package.get('driver','-')}", ln=True)
        pdf.cell(0, 6, f"Expected: {package.get('expected_date','-')}, Delivered: {package.get('delivered_date','-')}, Note: {package.get('delivery_note','-')}", ln=True)
        pdf.ln(3)
    
    pdf.output(filename)
    print(f"Packages exported successfully to {filename}!\n")
        
def admin_menu(user):
    while True:
        print("\nAdmin Menu")
        print("1. View All Users")
        print("2. Add New User")
        print("3. Delete User")
        print("4. View System Data")
        print("5. View Packages Status")
        print("6. View Delayed Deliveries")
        print("7. Export Packages to CSV")
        print("8. Export Packages to PDF")
        print("9. Logout")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            view_users()
        elif choice == 2:
            create_user()
        elif choice == 3:
            delete_user()
        elif choice == 4:
            view_system_data()
        elif choice == 5:
            view_package_status()
        elif choice == 6:
            view_delayed_packages()
        elif choice == 7:
            export_packages_csv()
        elif choice == 8:
            export_packages_pdf()
        elif choice == 9:
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")