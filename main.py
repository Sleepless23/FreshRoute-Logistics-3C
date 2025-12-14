from user import auth, add_user
from modules.admin_menu import admin_menu
from modules.dispatcher_menu import dispatcher_menu
from modules.driver_menu import driver_menu

def register():
    print("\nREGISTER STAFF ACCOUNT")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm_pass = input("Enter confirm password: ")
    
    if password != confirm_pass:
        print("Password and Confirmed aren't the same!\n")
        return
    
    print("\nSelect role:")
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
        print("Invalid role selected.\n")
        return
    
    role = roles[role_input]
    
    if add_user(username, password, role):
        print("Account created successfully!\n")
    else:
        print("Username is taken!\n")
        
def login():
    print("\nLOGIN")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = auth(username, password)
    
    if not user:
        print("Invalid credentials.\n")
        return None
    
    print(f"\nWelcome, {user.username}! (Role: {user.role})")
    return user

def main():
    while True:
        print("FreshRoute Logistics System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            user = login()
            if not user:
                continue
            
            if user.role == "admin":
                admin_menu(user)
            elif user.role == "dispatcher":
                dispatcher_menu(user)
            elif user.role == "driver":
                driver_menu(user)
                
        elif choice == 2:
            register()
            
        elif choice == 3:
            print("Bye-bye!")
            break
        
        else:
            print("Invalid choice.\n")
            
if __name__ == "__main__":
    main()