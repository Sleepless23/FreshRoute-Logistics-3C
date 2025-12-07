import json
from user import load_data, save_data, add_user

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
            
        print("User not found.\n")
            
    elif confirmation == 'n':
        print("Cancelled delete.\n")
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
        print("User created successfully!\n")
    else:
        print("Username already taken.\n")
        
def view_system_data():
    data = load_data()
    
    print("\nSYSTEM DATA")
    print(f"Total users: {len(data['users'])}")
    print(f"Total packages: {len(data['packages'])}")
    print(f"Total routes: {len(data['routes'])}")
    
    print()
    
def admin_menu(user):
    while True:
        print("\nADMIN MENU")
        print("1. View All Users")
        print("2. Add New User")
        print("3. Delete User")
        print("4. View System Data")
        print("5. Logout")
        
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
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")