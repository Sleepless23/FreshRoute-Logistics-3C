from user import auth, add_user
from modules.admin_menu import admin_menu
from modules.dispatcher_menu import dispatcher_menu
from modules.driver_menu import driver_menu

def register():
    print(f"\nREGISTER STAFF ACCOUNT\n{'-' * 100}")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm_pass = input("Enter confirm password: ")
    
    if password != confirm_pass:
        print("Password and Confirmed aren't the same!\n")
        return
    
    print(f"\nSelect role:\n{'-' * 100}")
    register_menu = ['Admin', 'Dispatcher', 'Driver']
    for i, r in zip(range(4), register_menu):
        print(f"{i + 1}. {r}")
    
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
    print(f"\nLOGIN\n{'-' * 100}")
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
        print(f"\nFreshRoute Logistics System\n{'-' * 100}")
        login_menu = ['Login', 'Register', 'Exit']
        for i, m in zip(range(4), login_menu):
            print(f"{i + 1}. {m}")
        
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                user = login()
                if not user:
                    continue
                match user.role:
                    case "admin":
                        admin_menu(user)
                    case "dispatcher":
                        dispatcher_menu(user)
                    case "driver":
                        driver_menu(user)        
            case 2:
                register()
            case 3:
                print("Bye-bye!")
                break
            case _:
                print("Invalid choice.\n")
            
if __name__ == "__main__":
    main()